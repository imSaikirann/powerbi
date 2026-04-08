CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id VARCHAR(20) PRIMARY KEY,
    employee_name VARCHAR(150) NOT NULL,
    age SMALLINT NOT NULL CHECK (age BETWEEN 18 AND 65),
    gender VARCHAR(30) NOT NULL,
    department_id INT NOT NULL REFERENCES departments(department_id),
    job_role VARCHAR(120) NOT NULL,
    salary NUMERIC(12, 2) NOT NULL CHECK (salary > 0),
    date_of_joining DATE NOT NULL,
    exit_date DATE NULL,
    attrition VARCHAR(3) NOT NULL CHECK (attrition IN ('Yes', 'No')),
    employment_status VARCHAR(20) NOT NULL,
    location_id INT NOT NULL REFERENCES locations(location_id)
);

CREATE TABLE IF NOT EXISTS performance_reviews (
    review_id BIGSERIAL PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL REFERENCES employees(employee_id),
    performance_rating SMALLINT NOT NULL CHECK (performance_rating BETWEEN 1 AND 5),
    review_period VARCHAR(20) NOT NULL DEFAULT 'FY2025'
);

CREATE TABLE IF NOT EXISTS attendance_summary (
    attendance_id BIGSERIAL PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL REFERENCES employees(employee_id),
    attendance_percentage NUMERIC(5, 2) NOT NULL CHECK (attendance_percentage BETWEEN 0 AND 100),
    summary_month DATE NOT NULL DEFAULT DATE_TRUNC('month', CURRENT_DATE)
);

CREATE INDEX IF NOT EXISTS idx_employees_department_id ON employees(department_id);
CREATE INDEX IF NOT EXISTS idx_employees_location_id ON employees(location_id);
CREATE INDEX IF NOT EXISTS idx_employees_date_of_joining ON employees(date_of_joining);
CREATE INDEX IF NOT EXISTS idx_employees_attrition ON employees(attrition);
CREATE INDEX IF NOT EXISTS idx_performance_employee_id ON performance_reviews(employee_id);
CREATE INDEX IF NOT EXISTS idx_attendance_employee_id ON attendance_summary(employee_id);
