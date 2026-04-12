from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
from sqlalchemy import create_engine, text

from scripts.clean_hr_data import main as clean_hr_data
from scripts.generate_hr_data import main as generate_hr_data
from scripts.train_attrition_model import main as train_attrition_model


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/hr_analytics")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
app = FastAPI(title="HR Analytics API", version="1.0.0")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN_DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned", "hr_employee_data_clean.csv")
QUALITY_REPORT_PATH = os.path.join(BASE_DIR, "data", "processed", "data_quality_report.json")
MODEL_REPORT_PATH = os.path.join(BASE_DIR, "data", "processed", "attrition_model_report.json")


def _load_json(path: str) -> dict[str, Any]:
    import json

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def _build_visual_payload() -> dict[str, Any]:
    frame = pd.read_csv(CLEAN_DATA_PATH)
    quality_report = _load_json(QUALITY_REPORT_PATH)
    model_report = _load_json(MODEL_REPORT_PATH)

    department_counts = (
        frame.groupby("department")["employee_id"]
        .count()
        .sort_values(ascending=False)
        .reset_index(name="count")
        .to_dict(orient="records")
    )
    attrition_split = (
        frame.groupby("attrition")["employee_id"]
        .count()
        .reset_index(name="count")
        .to_dict(orient="records")
    )
    hiring_trend = (
        frame.groupby("join_month")["employee_id"]
        .count()
        .reset_index(name="count")
        .sort_values("join_month")
        .tail(12)
        .to_dict(orient="records")
    )
    attendance_by_department = (
        frame.groupby("department")["attendance_percentage"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .reset_index(name="average_attendance")
        .to_dict(orient="records")
    )
    salary_by_department = (
        frame.groupby("department")["salary"]
        .mean()
        .round(0)
        .sort_values(ascending=False)
        .reset_index(name="average_salary")
        .to_dict(orient="records")
    )
    performance_by_department = (
        frame.groupby("department")["performance_rating"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .reset_index(name="average_performance")
        .to_dict(orient="records")
    )
    performance_scatter = (
        frame[
            [
                "employee_id",
                "department",
                "job_role",
                "attendance_percentage",
                "performance_rating",
                "salary",
            ]
        ]
        .sort_values(["department", "salary"], ascending=[True, False])
        .groupby("department", group_keys=False)
        .head(18)
        .reset_index(drop=True)
        .to_dict(orient="records")
    )
    performance_matrix = (
        frame.groupby(["department", "job_role"], as_index=False)
        .agg(
            employee_count=("employee_id", "count"),
            average_performance=("performance_rating", "mean"),
            average_attendance=("attendance_percentage", "mean"),
        )
        .round({"average_performance": 2, "average_attendance": 2})
        .sort_values(["department", "average_performance", "employee_count"], ascending=[True, False, False])
        .groupby("department", group_keys=False)
        .head(4)
        .to_dict(orient="records")
    )
    top_performing_department = performance_by_department[0]["department"] if performance_by_department else "N/A"

    return {
        "kpis": {
            "raw_rows": quality_report["input_rows"],
            "clean_rows": quality_report["output_rows"],
            "duplicates_removed": quality_report["duplicates_removed"],
            "attrition_rate": quality_report["attrition_rate_percent"],
            "average_attendance": quality_report["average_attendance_percent"],
            "roc_auc": model_report["roc_auc"],
            "average_performance": round(float(frame["performance_rating"].mean()), 2),
            "top_performing_department": top_performing_department,
        },
        "charts": {
            "department_counts": department_counts,
            "attrition_split": attrition_split,
            "hiring_trend": hiring_trend,
            "attendance_by_department": attendance_by_department,
            "salary_by_department": salary_by_department,
            "performance_by_department": performance_by_department,
            "performance_scatter": performance_scatter,
            "performance_matrix": performance_matrix,
        },
        "sample_rows": frame.head(10).to_dict(orient="records"),
    }


def _run_pipeline() -> dict[str, Any]:
    generate_hr_data()
    clean_hr_data()
    train_attrition_model()
    return _build_visual_payload()


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HR Analytics Runner</title>
  <style>
    :root {
      --bg: #f5efe6;
      --card: #fffdf9;
      --ink: #213547;
      --muted: #667784;
      --accent: #0f766e;
      --accent-soft: #d7f3ee;
      --danger: #c2410c;
      --border: #dfd5c7;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Segoe UI", Tahoma, sans-serif;
      background:
        radial-gradient(circle at top right, #d9efe8 0, transparent 28%),
        linear-gradient(180deg, #f8f2ea 0%, var(--bg) 100%);
      color: var(--ink);
    }
    .wrap {
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }
    .hero {
      background: rgba(255,255,255,0.68);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 28px;
      backdrop-filter: blur(6px);
      box-shadow: 0 10px 30px rgba(33,53,71,0.08);
    }
    h1, h2 {
      margin: 0 0 12px;
    }
    p {
      color: var(--muted);
      line-height: 1.6;
    }
    .actions {
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
      margin-top: 18px;
    }
    button {
      border: 0;
      border-radius: 999px;
      background: var(--accent);
      color: white;
      padding: 14px 20px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 10px 18px rgba(15,118,110,0.22);
    }
    button:disabled {
      opacity: 0.7;
      cursor: progress;
    }
    .status {
      font-weight: 600;
      color: var(--ink);
    }
    .page-switcher {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 24px;
    }
    .page-chip {
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 10px 16px;
      background: rgba(255,255,255,0.82);
      color: var(--ink);
      font-weight: 700;
      cursor: pointer;
      box-shadow: none;
    }
    .page-chip.active {
      background: var(--accent);
      color: white;
      border-color: var(--accent);
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 26px;
    }
    .card, .panel {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 18px;
      box-shadow: 0 10px 24px rgba(33,53,71,0.06);
    }
    .metric-label {
      color: var(--muted);
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .metric-value {
      margin-top: 8px;
      font-size: 30px;
      font-weight: 800;
    }
    .panels {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 24px;
    }
    .page {
      display: none;
      margin-top: 22px;
    }
    .page.active {
      display: block;
    }
    .chart {
      margin-top: 14px;
      display: grid;
      gap: 10px;
    }
    .bar-row {
      display: grid;
      grid-template-columns: 120px 1fr 56px;
      gap: 10px;
      align-items: center;
      font-size: 14px;
    }
    .bar-track {
      height: 12px;
      background: #eee5d9;
      border-radius: 999px;
      overflow: hidden;
    }
    .bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent), #34b3a0);
      border-radius: 999px;
    }
    .mini-line {
      width: 100%;
      height: 220px;
      margin-top: 10px;
      background: linear-gradient(180deg, #fcfaf6 0%, #f2ece3 100%);
      border-radius: 18px;
      border: 1px solid #eadfce;
    }
    .scatter-wrap {
      margin-top: 12px;
      overflow: hidden;
    }
    .scatter-chart {
      width: 100%;
      height: 320px;
      background: linear-gradient(180deg, #fcfaf6 0%, #f2ece3 100%);
      border-radius: 18px;
      border: 1px solid #eadfce;
    }
    .legend {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 14px;
      font-size: 12px;
      color: var(--muted);
    }
    .legend-item {
      display: inline-flex;
      gap: 8px;
      align-items: center;
    }
    .legend-swatch {
      width: 10px;
      height: 10px;
      border-radius: 999px;
      display: inline-block;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      font-size: 13px;
    }
    th, td {
      text-align: left;
      padding: 10px 8px;
      border-bottom: 1px solid #efe5d8;
    }
    th {
      color: var(--muted);
      font-weight: 700;
    }
    .hidden { display: none; }
    @media (max-width: 700px) {
      .bar-row { grid-template-columns: 90px 1fr 46px; font-size: 12px; }
      .metric-value { font-size: 24px; }
      .page-switcher { gap: 8px; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <h1>HR Analytics One-Click Runner</h1>
      <p>Use one button to generate synthetic employee data, clean it, train the attrition model, and immediately view the output through KPI cards, charts, and sample rows.</p>
      <div class="actions">
        <button id="runBtn">Generate, Clean, and Train</button>
        <div id="status" class="status">Ready to run the pipeline.</div>
      </div>
    </section>

    <section id="results" class="hidden">
      <div class="page-switcher">
        <button type="button" class="page-chip active" data-page="overviewPage">Executive Overview</button>
        <button type="button" class="page-chip" data-page="performancePage">Workforce Performance</button>
      </div>

      <div id="overviewPage" class="page active">
        <div id="kpiGrid" class="grid"></div>
        <div class="panels">
          <div class="panel">
            <h2>Department Headcount</h2>
            <p>Employee distribution after cleaning.</p>
            <div id="departmentChart" class="chart"></div>
          </div>
          <div class="panel">
            <h2>Attrition Split</h2>
            <p>Employees who stayed versus employees who left.</p>
            <div id="attritionChart" class="chart"></div>
          </div>
          <div class="panel">
            <h2>Monthly Hiring Trend</h2>
            <p>Last 12 join-month counts from the cleaned data.</p>
            <svg id="hiringLine" class="mini-line" viewBox="0 0 640 220" preserveAspectRatio="none"></svg>
          </div>
          <div class="panel">
            <h2>Average Attendance by Department</h2>
            <p>Department-level attendance after imputation and cleaning.</p>
            <div id="attendanceChart" class="chart"></div>
          </div>
          <div class="panel">
            <h2>Average Salary by Department</h2>
            <p>Department-wise average salary from the cleaned dataset.</p>
            <div id="salaryChart" class="chart"></div>
          </div>
          <div class="panel">
            <h2>Sample Cleaned Output</h2>
            <p>Preview of the top rows that feed reporting and modeling.</p>
            <div style="overflow:auto;">
              <table id="sampleTable"></table>
            </div>
          </div>
        </div>
      </div>

      <div id="performancePage" class="page">
        <div id="performanceKpiGrid" class="grid"></div>
        <div class="panels">
          <div class="panel">
            <h2>Department-Wise Performance</h2>
            <p>Average performance rating across departments.</p>
            <div id="performanceDepartmentChart" class="chart"></div>
          </div>
          <div class="panel">
            <h2>Attendance vs Performance</h2>
            <p>High-salary employees are shown with larger markers to highlight concentration by department.</p>
            <div class="scatter-wrap">
              <svg id="performanceScatter" class="scatter-chart" viewBox="0 0 640 320" preserveAspectRatio="none"></svg>
            </div>
            <div id="performanceLegend" class="legend"></div>
          </div>
          <div class="panel" style="grid-column: 1 / -1;">
            <h2>Department and Role Matrix</h2>
            <p>Top roles per department with employee count, average performance, and average attendance.</p>
            <div style="overflow:auto;">
              <table id="performanceMatrixTable"></table>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <script>
    const runBtn = document.getElementById("runBtn");
    const statusEl = document.getElementById("status");
    const resultsEl = document.getElementById("results");
    const pageChips = Array.from(document.querySelectorAll(".page-chip"));

    runBtn.addEventListener("click", async () => {
      runBtn.disabled = true;
      statusEl.textContent = "Running pipeline: generating data, cleaning records, training model...";
      try {
        const response = await fetch("/pipeline/run", { method: "POST" });
        const payload = await response.json();
        if (!response.ok) throw new Error(payload.detail || "Pipeline failed.");
        render(payload);
        resultsEl.classList.remove("hidden");
        statusEl.textContent = "Pipeline completed successfully. Charts and outputs are ready below.";
      } catch (error) {
        statusEl.textContent = error.message;
      } finally {
        runBtn.disabled = false;
      }
    });

    pageChips.forEach((chip) => {
      chip.addEventListener("click", () => setActivePage(chip.dataset.page));
    });

    function render(payload) {
      renderKpis(payload.kpis);
      renderBars("departmentChart", payload.charts.department_counts, "department", "count");
      renderBars("attritionChart", payload.charts.attrition_split, "attrition", "count");
      renderBars("attendanceChart", payload.charts.attendance_by_department, "department", "average_attendance", "%");
      renderBars("salaryChart", payload.charts.salary_by_department, "department", "average_salary");
      renderBars("performanceDepartmentChart", payload.charts.performance_by_department, "department", "average_performance");
      renderLine(payload.charts.hiring_trend);
      renderTable(payload.sample_rows);
      renderPerformanceKpis(payload.kpis, payload.charts.performance_by_department);
      renderScatter(payload.charts.performance_scatter);
      renderPerformanceMatrix(payload.charts.performance_matrix);
    }

    function renderKpis(kpis) {
      const items = [
        ["Raw Rows", kpis.raw_rows],
        ["Clean Rows", kpis.clean_rows],
        ["Duplicates Removed", kpis.duplicates_removed],
        ["Attrition Rate", `${kpis.attrition_rate}%`],
        ["Average Attendance", `${kpis.average_attendance}%`],
        ["ROC AUC", kpis.roc_auc]
      ];
      document.getElementById("kpiGrid").innerHTML = items.map(([label, value]) => `
        <div class="card">
          <div class="metric-label">${label}</div>
          <div class="metric-value">${value}</div>
        </div>
      `).join("");
    }

    function renderPerformanceKpis(kpis, performanceRows) {
      const highestScore = performanceRows.length ? performanceRows[0].average_performance : 0;
      const lowestScore = performanceRows.length ? performanceRows[performanceRows.length - 1].average_performance : 0;
      const items = [
        ["Average Performance", kpis.average_performance],
        ["Top Department", kpis.top_performing_department],
        ["Best Dept Score", highestScore],
        ["Lowest Dept Score", lowestScore]
      ];
      document.getElementById("performanceKpiGrid").innerHTML = items.map(([label, value]) => `
        <div class="card">
          <div class="metric-label">${label}</div>
          <div class="metric-value">${value}</div>
        </div>
      `).join("");
    }

    function renderBars(targetId, rows, labelKey, valueKey, suffix = "") {
      const target = document.getElementById(targetId);
      const max = Math.max(...rows.map(row => Number(row[valueKey]) || 0), 1);
      target.innerHTML = rows.map(row => {
        const value = Number(row[valueKey]) || 0;
        const width = (value / max) * 100;
        return `
          <div class="bar-row">
            <div>${row[labelKey]}</div>
            <div class="bar-track"><div class="bar-fill" style="width:${width}%"></div></div>
            <div>${formatValue(value)}${suffix}</div>
          </div>
        `;
      }).join("");
    }

    function renderLine(rows) {
      const svg = document.getElementById("hiringLine");
      const width = 640;
      const height = 220;
      const padding = 24;
      const max = Math.max(...rows.map(row => Number(row.count) || 0), 1);
      const min = Math.min(...rows.map(row => Number(row.count) || 0), 0);
      const span = Math.max(max - min, 1);
      const stepX = (width - padding * 2) / Math.max(rows.length - 1, 1);
      const points = rows.map((row, index) => {
        const x = padding + index * stepX;
        const y = height - padding - ((row.count - min) / span) * (height - padding * 2);
        return `${x},${y}`;
      }).join(" ");
      const labels = rows.map((row, index) => {
        const x = padding + index * stepX;
        return `<text x="${x}" y="${height - 8}" font-size="10" text-anchor="middle" fill="#667784">${row.join_month}</text>`;
      }).join("");
      const dots = rows.map((row, index) => {
        const x = padding + index * stepX;
        const y = height - padding - ((row.count - min) / span) * (height - padding * 2);
        return `<circle cx="${x}" cy="${y}" r="4" fill="#0f766e"></circle>`;
      }).join("");
      svg.innerHTML = `
        <polyline fill="none" stroke="#7dc8ba" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" points="${points}" opacity="0.18"></polyline>
        <polyline fill="none" stroke="#0f766e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" points="${points}"></polyline>
        ${dots}
        ${labels}
      `;
    }

    function renderScatter(rows) {
      const svg = document.getElementById("performanceScatter");
      const legend = document.getElementById("performanceLegend");
      const width = 640;
      const height = 320;
      const padding = { top: 24, right: 24, bottom: 36, left: 52 };
      const departments = [...new Set(rows.map(row => row.department))];
      const palette = ["#0f766e", "#2563eb", "#d97706", "#dc2626", "#7c3aed", "#0891b2", "#4f46e5"];
      const colors = Object.fromEntries(departments.map((department, index) => [department, palette[index % palette.length]]));
      const xMin = 55;
      const xMax = 100;
      const yMin = 1;
      const yMax = 5;
      const salaryMax = Math.max(...rows.map(row => Number(row.salary) || 0), 1);
      const xScale = (value) => padding.left + ((value - xMin) / (xMax - xMin)) * (width - padding.left - padding.right);
      const yScale = (value) => height - padding.bottom - ((value - yMin) / (yMax - yMin)) * (height - padding.top - padding.bottom);

      const gridLines = [60, 70, 80, 90, 100].map(value => `
        <g>
          <line x1="${xScale(value)}" y1="${padding.top}" x2="${xScale(value)}" y2="${height - padding.bottom}" stroke="#e4d9ca" stroke-dasharray="4 6"></line>
          <text x="${xScale(value)}" y="${height - 12}" text-anchor="middle" fill="#667784" font-size="10">${value}%</text>
        </g>
      `).join("") + [1, 2, 3, 4, 5].map(value => `
        <g>
          <line x1="${padding.left}" y1="${yScale(value)}" x2="${width - padding.right}" y2="${yScale(value)}" stroke="#ece2d5" stroke-dasharray="4 6"></line>
          <text x="${padding.left - 16}" y="${yScale(value) + 4}" text-anchor="end" fill="#667784" font-size="10">${value}</text>
        </g>
      `).join("");

      const points = rows.map((row) => {
        const radius = 4 + ((Number(row.salary) || 0) / salaryMax) * 8;
        const x = xScale(Number(row.attendance_percentage) || xMin);
        const y = yScale(Number(row.performance_rating) || yMin);
        const title = `${row.job_role} (${row.department}) | Attendance: ${row.attendance_percentage}% | Performance: ${row.performance_rating} | Salary: ${formatValue(Number(row.salary) || 0)}`;
        return `
          <circle cx="${x}" cy="${y}" r="${radius}" fill="${colors[row.department]}" fill-opacity="0.72" stroke="white" stroke-width="1.5">
            <title>${title}</title>
          </circle>
        `;
      }).join("");

      svg.innerHTML = `
        ${gridLines}
        <line x1="${padding.left}" y1="${height - padding.bottom}" x2="${width - padding.right}" y2="${height - padding.bottom}" stroke="#9eaab3"></line>
        <line x1="${padding.left}" y1="${padding.top}" x2="${padding.left}" y2="${height - padding.bottom}" stroke="#9eaab3"></line>
        <text x="${width / 2}" y="${height - 2}" text-anchor="middle" fill="#667784" font-size="11">Attendance Percentage</text>
        <text x="14" y="${height / 2}" text-anchor="middle" fill="#667784" font-size="11" transform="rotate(-90 14 ${height / 2})">Performance Rating</text>
        ${points}
      `;

      legend.innerHTML = departments.map((department) => `
        <span class="legend-item">
          <span class="legend-swatch" style="background:${colors[department]}"></span>
          <span>${department}</span>
        </span>
      `).join("");
    }

    function renderPerformanceMatrix(rows) {
      const table = document.getElementById("performanceMatrixTable");
      if (!rows.length) {
        table.innerHTML = "<tr><td>No performance rows available.</td></tr>";
        return;
      }
      const headHtml = `
        <tr>
          <th>Department</th>
          <th>Job Role</th>
          <th>Employees</th>
          <th>Avg Performance</th>
          <th>Avg Attendance</th>
        </tr>
      `;
      const bodyHtml = rows.map((row) => `
        <tr>
          <td>${row.department}</td>
          <td>${row.job_role}</td>
          <td>${row.employee_count}</td>
          <td>${row.average_performance}</td>
          <td>${row.average_attendance}%</td>
        </tr>
      `).join("");
      table.innerHTML = `<thead>${headHtml}</thead><tbody>${bodyHtml}</tbody>`;
    }

    function renderTable(rows) {
      const table = document.getElementById("sampleTable");
      if (!rows.length) {
        table.innerHTML = "<tr><td>No rows available.</td></tr>";
        return;
      }
      const headers = Object.keys(rows[0]).slice(0, 8);
      const headHtml = `<tr>${headers.map(h => `<th>${h}</th>`).join("")}</tr>`;
      const bodyHtml = rows.map(row => `<tr>${headers.map(h => `<td>${row[h] ?? ""}</td>`).join("")}</tr>`).join("");
      table.innerHTML = `<thead>${headHtml}</thead><tbody>${bodyHtml}</tbody>`;
    }

    function setActivePage(pageId) {
      document.querySelectorAll(".page").forEach((page) => {
        page.classList.toggle("active", page.id === pageId);
      });
      pageChips.forEach((chip) => {
        chip.classList.toggle("active", chip.dataset.page === pageId);
      });
    }

    function formatValue(value) {
      if (value >= 1000) return Intl.NumberFormat().format(Math.round(value));
      if (Number.isInteger(value)) return value;
      return value.toFixed(2);
    }
  </script>
</body>
</html>
"""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/pipeline/status")
def pipeline_status() -> dict[str, Any]:
    if not (
        os.path.exists(CLEAN_DATA_PATH)
        and os.path.exists(QUALITY_REPORT_PATH)
        and os.path.exists(MODEL_REPORT_PATH)
    ):
        raise HTTPException(status_code=404, detail="Pipeline outputs are not available yet.")
    return _build_visual_payload()


@app.post("/pipeline/run")
def run_pipeline() -> dict[str, Any]:
    try:
        return _run_pipeline()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {exc}") from exc


@app.get("/employees")
def get_employees(limit: int = 100) -> list[dict[str, Any]]:
    query = text(
        """
        SELECT
            employee_id,
            employee_name,
            age,
            gender,
            department_name,
            job_role,
            salary,
            date_of_joining,
            exit_date,
            attrition,
            employment_status,
            location_name,
            performance_rating,
            attendance_percentage
        FROM vw_hr_employee_snapshot
        ORDER BY employee_id
        LIMIT :limit
        """
    )
    with engine.connect() as connection:
        rows = connection.execute(query, {"limit": limit}).mappings().all()
    return [dict(row) for row in rows]


@app.get("/kpis")
def get_kpis() -> dict[str, Any]:
    query = text("SELECT * FROM vw_hr_kpis")
    with engine.connect() as connection:
        row = connection.execute(query).mappings().first()
    if row is None:
        raise HTTPException(status_code=404, detail="KPI view returned no data.")
    return dict(row)
