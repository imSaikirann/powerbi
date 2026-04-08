CREATE OR REPLACE VIEW vw_hr_employee_snapshot AS
SELECT
    e.employee_id,
    e.employee_name,
    e.age,
    e.gender,
    d.department_name,
    e.job_role,
    e.salary,
    e.date_of_joining,
    e.exit_date,
    e.attrition,
    e.employment_status,
    l.location_name,
    p.performance_rating,
    a.attendance_percentage
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN locations l ON l.location_id = e.location_id
LEFT JOIN performance_reviews p ON p.employee_id = e.employee_id
LEFT JOIN attendance_summary a ON a.employee_id = e.employee_id;

CREATE OR REPLACE VIEW vw_hr_kpis AS
SELECT
    COUNT(*) AS total_employees,
    ROUND(100.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS attrition_rate_percent,
    ROUND(AVG(salary), 2) AS avg_salary,
    ROUND(AVG(EXTRACT(DAY FROM (COALESCE(exit_date, CURRENT_DATE) - date_of_joining)) / 365.25), 2) AS avg_tenure_years
FROM employees;
