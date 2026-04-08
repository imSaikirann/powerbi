from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import random

import numpy as np
import pandas as pd
from faker import Faker


faker = Faker()
random.seed(42)
np.random.seed(42)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "hr_employee_data_raw.csv"


@dataclass(frozen=True)
class DepartmentSpec:
    name: str
    headcount_share: float
    salary_min: int
    salary_max: int
    roles: Dict[str, float]


DEPARTMENTS: List[DepartmentSpec] = [
    DepartmentSpec(
        name="Engineering",
        headcount_share=0.24,
        salary_min=70000,
        salary_max=180000,
        roles={
            "Software Engineer": 0.40,
            "Senior Engineer": 0.25,
            "QA Engineer": 0.12,
            "Data Engineer": 0.13,
            "Engineering Manager": 0.10,
        },
    ),
    DepartmentSpec(
        name="Sales",
        headcount_share=0.18,
        salary_min=45000,
        salary_max=150000,
        roles={
            "Sales Executive": 0.38,
            "Account Manager": 0.24,
            "Sales Manager": 0.14,
            "Business Development Rep": 0.18,
            "Regional Director": 0.06,
        },
    ),
    DepartmentSpec(
        name="Human Resources",
        headcount_share=0.10,
        salary_min=40000,
        salary_max=110000,
        roles={
            "HR Coordinator": 0.24,
            "Recruiter": 0.28,
            "HR Generalist": 0.24,
            "HR Manager": 0.16,
            "People Operations Lead": 0.08,
        },
    ),
    DepartmentSpec(
        name="Finance",
        headcount_share=0.10,
        salary_min=50000,
        salary_max=140000,
        roles={
            "Financial Analyst": 0.36,
            "Accountant": 0.30,
            "Finance Manager": 0.16,
            "Payroll Specialist": 0.12,
            "Controller": 0.06,
        },
    ),
    DepartmentSpec(
        name="Marketing",
        headcount_share=0.11,
        salary_min=45000,
        salary_max=135000,
        roles={
            "Marketing Specialist": 0.30,
            "Content Strategist": 0.18,
            "SEO Analyst": 0.16,
            "Marketing Manager": 0.24,
            "Brand Director": 0.12,
        },
    ),
    DepartmentSpec(
        name="Operations",
        headcount_share=0.15,
        salary_min=38000,
        salary_max=120000,
        roles={
            "Operations Analyst": 0.28,
            "Operations Specialist": 0.28,
            "Program Manager": 0.18,
            "Operations Manager": 0.18,
            "Director of Operations": 0.08,
        },
    ),
    DepartmentSpec(
        name="Customer Support",
        headcount_share=0.12,
        salary_min=32000,
        salary_max=90000,
        roles={
            "Support Associate": 0.42,
            "Customer Success Manager": 0.22,
            "Technical Support Engineer": 0.18,
            "Support Lead": 0.12,
            "Head of Support": 0.06,
        },
    ),
]

LOCATIONS = {
    "Bengaluru": 0.24,
    "Hyderabad": 0.16,
    "Mumbai": 0.14,
    "Pune": 0.11,
    "Chennai": 0.10,
    "Delhi": 0.11,
    "Kolkata": 0.07,
    "Remote": 0.07,
}

GENDERS = {"Male": 0.54, "Female": 0.43, "Non-Binary": 0.03}


def weighted_choice(options: Dict[str, float]) -> str:
    values = list(options.keys())
    probabilities = list(options.values())
    return np.random.choice(values, p=probabilities)


def sample_department() -> DepartmentSpec:
    probabilities = [department.headcount_share for department in DEPARTMENTS]
    return DEPARTMENTS[np.random.choice(len(DEPARTMENTS), p=probabilities)]


def derive_performance(department_name: str) -> int:
    performance_weights = {
        "Engineering": [0.05, 0.15, 0.38, 0.28, 0.14],
        "Sales": [0.08, 0.17, 0.32, 0.28, 0.15],
        "Human Resources": [0.04, 0.12, 0.40, 0.30, 0.14],
        "Finance": [0.03, 0.12, 0.36, 0.31, 0.18],
        "Marketing": [0.06, 0.16, 0.36, 0.27, 0.15],
        "Operations": [0.07, 0.16, 0.40, 0.25, 0.12],
        "Customer Support": [0.10, 0.18, 0.40, 0.22, 0.10],
    }
    return int(np.random.choice([1, 2, 3, 4, 5], p=performance_weights[department_name]))


def derive_attendance(performance_rating: int, tenure_years: float, attrition_bias: float) -> float:
    baseline = 82 + (performance_rating * 2.7) + min(tenure_years, 10) * 0.4 - attrition_bias * 12
    attendance = np.random.normal(loc=baseline, scale=4.5)
    return float(np.clip(round(attendance, 2), 55, 100))


def derive_salary(spec: DepartmentSpec, job_role: str, age: int, performance_rating: int, tenure_years: float) -> int:
    role_multipliers = {
        "Manager": 1.35,
        "Director": 1.65,
        "Lead": 1.30,
        "Senior": 1.22,
        "Head": 1.70,
    }
    multiplier = 1.0
    for keyword, role_multiplier in role_multipliers.items():
        if keyword in job_role:
            multiplier = max(multiplier, role_multiplier)
    experience_factor = 1 + min(tenure_years / 12, 0.22) + max(age - 30, 0) / 180
    performance_factor = 0.92 + performance_rating * 0.04
    raw_salary = np.random.uniform(spec.salary_min, spec.salary_max) * multiplier * experience_factor * performance_factor
    salary = int(round(min(raw_salary, spec.salary_max * 1.65), -2))
    return salary


def derive_attrition(performance_rating: int, attendance_percentage: float, tenure_years: float, salary: int, spec: DepartmentSpec) -> str:
    salary_midpoint = (spec.salary_min + spec.salary_max) / 2
    salary_penalty = max(0, (salary_midpoint - salary) / salary_midpoint) * 0.10
    tenure_risk = 0.12 if tenure_years < 1.5 else 0.05 if tenure_years < 3 else -0.02
    performance_risk = {1: 0.24, 2: 0.15, 3: 0.08, 4: 0.04, 5: 0.02}[performance_rating]
    attendance_risk = max(0, (88 - attendance_percentage) / 100)
    department_risk = {
        "Sales": 0.06,
        "Customer Support": 0.07,
        "Operations": 0.04,
        "Marketing": 0.03,
        "Engineering": 0.02,
        "Human Resources": 0.02,
        "Finance": 0.01,
    }[spec.name]
    attrition_probability = min(0.55, max(0.02, performance_risk + attendance_risk + tenure_risk + salary_penalty + department_risk))
    return "Yes" if np.random.random() < attrition_probability else "No"


def generate_employee_row(employee_number: int) -> dict:
    department_spec = sample_department()
    age = int(np.clip(np.random.normal(loc=34, scale=7.5), 21, 60))
    gender = weighted_choice(GENDERS)
    location = weighted_choice(LOCATIONS)
    job_role = weighted_choice(department_spec.roles)
    join_date = faker.date_between(start_date="-10y", end_date="today")
    tenure_years = (pd.Timestamp.today().normalize() - pd.Timestamp(join_date)).days / 365.25
    performance_rating = derive_performance(department_spec.name)
    attrition_bias = max(0, 0.24 - (performance_rating * 0.035))
    attendance_percentage = derive_attendance(performance_rating, tenure_years, attrition_bias)
    salary = derive_salary(department_spec, job_role, age, performance_rating, tenure_years)
    attrition = derive_attrition(performance_rating, attendance_percentage, tenure_years, salary, department_spec)

    exit_date = None
    if attrition == "Yes":
        exit_offset_days = np.random.randint(180, max(181, (pd.Timestamp.today().normalize() - pd.Timestamp(join_date)).days))
        exit_date = pd.Timestamp(join_date) + pd.Timedelta(days=int(exit_offset_days))
        exit_date = min(exit_date, pd.Timestamp.today().normalize() - pd.Timedelta(days=np.random.randint(1, 60)))

    return {
        "employee_id": f"EMP{employee_number:05d}",
        "name": faker.name(),
        "age": age,
        "gender": gender,
        "department": department_spec.name,
        "job_role": job_role,
        "salary": salary,
        "date_of_joining": pd.Timestamp(join_date).date().isoformat(),
        "exit_date": exit_date.date().isoformat() if exit_date is not None else None,
        "attrition": attrition,
        "performance_rating": performance_rating,
        "attendance_percentage": attendance_percentage,
        "location": location,
    }


def inject_realistic_quality_issues(frame: pd.DataFrame) -> pd.DataFrame:
    dirty = frame.copy()

    duplicate_rows = dirty.sample(n=35, random_state=42)
    dirty = pd.concat([dirty, duplicate_rows], ignore_index=True)

    salary_missing_idx = dirty.sample(frac=0.012, random_state=2).index
    attendance_missing_idx = dirty.sample(frac=0.015, random_state=3).index
    gender_missing_idx = dirty.sample(frac=0.005, random_state=4).index
    dirty.loc[salary_missing_idx, "salary"] = np.nan
    dirty.loc[attendance_missing_idx, "attendance_percentage"] = np.nan
    dirty.loc[gender_missing_idx, "gender"] = None

    inconsistent_department_idx = dirty.sample(frac=0.01, random_state=5).index
    dirty.loc[inconsistent_department_idx, "department"] = dirty.loc[inconsistent_department_idx, "department"].str.lower()

    inconsistent_attrition_idx = dirty.sample(frac=0.01, random_state=6).index
    dirty.loc[inconsistent_attrition_idx, "attrition"] = dirty.loc[inconsistent_attrition_idx, "attrition"].str.lower()

    return dirty


def main(record_count: int = 6000) -> None:
    rows = [generate_employee_row(employee_number=i) for i in range(1, record_count + 1)]
    hr_frame = pd.DataFrame(rows)
    dirty_hr_frame = inject_realistic_quality_issues(hr_frame)
    RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    dirty_hr_frame.to_csv(RAW_DATA_PATH, index=False)
    print(f"Raw HR dataset created at {RAW_DATA_PATH} with {len(dirty_hr_frame):,} rows.")


if __name__ == "__main__":
    main()
