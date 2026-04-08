from __future__ import annotations

from pathlib import Path
import json

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "hr_employee_data_raw.csv"
CLEAN_DATA_PATH = BASE_DIR / "data" / "cleaned" / "hr_employee_data_clean.csv"
QUALITY_REPORT_PATH = BASE_DIR / "data" / "processed" / "data_quality_report.json"


def title_case_department(value: str) -> str:
    normalized = value.strip().lower()
    mappings = {
        "human resources": "Human Resources",
        "customer support": "Customer Support",
    }
    return mappings.get(normalized, normalized.title())


def normalize_attrition(value: str) -> str:
    return "Yes" if str(value).strip().lower() == "yes" else "No"


def clean_dataset(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    initial_rows = len(frame)
    frame = frame.drop_duplicates().copy()
    duplicates_removed = initial_rows - len(frame)

    frame["date_of_joining"] = pd.to_datetime(frame["date_of_joining"], errors="coerce")
    frame["exit_date"] = pd.to_datetime(frame["exit_date"], errors="coerce")
    frame["department"] = frame["department"].astype(str).map(title_case_department)
    frame["gender"] = frame["gender"].fillna("Undisclosed").astype(str).str.strip().str.title()
    frame["location"] = frame["location"].astype(str).str.strip().str.title()
    frame["job_role"] = frame["job_role"].astype(str).str.strip()
    frame["attrition"] = frame["attrition"].astype(str).map(normalize_attrition)

    department_salary_medians = frame.groupby("department")["salary"].transform("median")
    frame["salary"] = frame["salary"].fillna(department_salary_medians)

    department_attendance_medians = frame.groupby("department")["attendance_percentage"].transform("median")
    frame["attendance_percentage"] = frame["attendance_percentage"].fillna(department_attendance_medians)

    frame["salary"] = frame["salary"].round(0).astype(int)
    frame["attendance_percentage"] = frame["attendance_percentage"].round(2).clip(lower=0, upper=100)
    frame["performance_rating"] = frame["performance_rating"].astype(int).clip(lower=1, upper=5)
    frame["age"] = frame["age"].astype(int).clip(lower=18, upper=65)

    frame["tenure_years"] = (
        ((frame["exit_date"].fillna(pd.Timestamp.today().normalize()) - frame["date_of_joining"]).dt.days) / 365.25
    ).round(2)
    frame["employment_status"] = frame["attrition"].map({"Yes": "Inactive", "No": "Active"})
    frame["join_year"] = frame["date_of_joining"].dt.year.astype(int)
    frame["join_month"] = frame["date_of_joining"].dt.to_period("M").astype(str)

    quality_report = {
        "input_rows": initial_rows,
        "output_rows": int(len(frame)),
        "duplicates_removed": int(duplicates_removed),
        "missing_values_after_cleaning": frame.isna().sum().to_dict(),
        "attrition_rate_percent": round((frame["attrition"].eq("Yes").mean() * 100), 2),
        "average_attendance_percent": round(frame["attendance_percentage"].mean(), 2),
    }
    return frame, quality_report


def main() -> None:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Missing raw dataset at {RAW_DATA_PATH}. Run generate_hr_data.py first.")

    raw_frame = pd.read_csv(RAW_DATA_PATH)
    clean_frame, quality_report = clean_dataset(raw_frame)

    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUALITY_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    clean_frame.to_csv(CLEAN_DATA_PATH, index=False)
    QUALITY_REPORT_PATH.write_text(json.dumps(quality_report, indent=2), encoding="utf-8")
    print(f"Clean HR dataset created at {CLEAN_DATA_PATH} with {len(clean_frame):,} rows.")
    print(f"Quality report written to {QUALITY_REPORT_PATH}.")


if __name__ == "__main__":
    main()
