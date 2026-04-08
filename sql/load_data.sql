-- Run after schema.sql.
-- Update the CSV path to match your local PostgreSQL server file access or use \copy from psql.

CREATE TEMP TABLE staging_hr_employees (
    employee_id VARCHAR(20),
    name VARCHAR(150),
    age SMALLINT,
    gender VARCHAR(30),
    department VARCHAR(100),
    job_role VARCHAR(120),
    salary NUMERIC(12, 2),
    date_of_joining DATE,
    exit_date DATE,
    attrition VARCHAR(3),
    performance_rating SMALLINT,
    attendance_percentage NUMERIC(5, 2),
    location VARCHAR(100),
    tenure_years NUMERIC(8, 2),
    employment_status VARCHAR(20),
    join_year INT,
    join_month VARCHAR(10)
);

-- Example psql command:
-- \copy staging_hr_employees FROM 'data/cleaned/hr_employee_data_clean.csv' DELIMITER ',' CSV HEADER;

INSERT INTO departments (department_name)
SELECT DISTINCT department
FROM staging_hr_employees
WHERE department IS NOT NULL
ON CONFLICT (department_name) DO NOTHING;

INSERT INTO locations (location_name)
SELECT DISTINCT location
FROM staging_hr_employees
WHERE location IS NOT NULL
ON CONFLICT (location_name) DO NOTHING;

INSERT INTO employees (
    employee_id,
    employee_name,
    age,
    gender,
    department_id,
    job_role,
    salary,
    date_of_joining,
    exit_date,
    attrition,
    employment_status,
    location_id
)
SELECT
    s.employee_id,
    s.name,
    s.age,
    s.gender,
    d.department_id,
    s.job_role,
    s.salary,
    s.date_of_joining,
    s.exit_date,
    s.attrition,
    s.employment_status,
    l.location_id
FROM staging_hr_employees s
JOIN departments d ON d.department_name = s.department
JOIN locations l ON l.location_name = s.location
ON CONFLICT (employee_id) DO NOTHING;

INSERT INTO performance_reviews (employee_id, performance_rating, review_period)
SELECT employee_id, performance_rating, 'FY2025'
FROM staging_hr_employees;

INSERT INTO attendance_summary (employee_id, attendance_percentage, summary_month)
SELECT employee_id, attendance_percentage, DATE '2025-12-01'
FROM staging_hr_employees;
