from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/hr_analytics")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
app = FastAPI(title="HR Analytics API", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


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
