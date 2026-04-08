-- Total headcount
SELECT COUNT(*) AS total_employees
FROM employees;

-- Attrition rate
SELECT ROUND(100.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS attrition_rate_percent
FROM employees;

-- Average tenure in years
SELECT ROUND(AVG(EXTRACT(DAY FROM (COALESCE(exit_date, CURRENT_DATE) - date_of_joining)) / 365.25), 2) AS avg_tenure_years
FROM employees;

-- Headcount by department
SELECT
    d.department_name,
    COUNT(*) AS headcount
FROM employees e
JOIN departments d ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY headcount DESC;

-- Average salary per department
SELECT
    d.department_name,
    ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN departments d ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- Monthly hiring trends
SELECT
    DATE_TRUNC('month', date_of_joining)::date AS hiring_month,
    COUNT(*) AS hires
FROM employees
GROUP BY DATE_TRUNC('month', date_of_joining)
ORDER BY hiring_month;

-- Performance distribution
SELECT
    performance_rating,
    COUNT(*) AS employees
FROM performance_reviews
GROUP BY performance_rating
ORDER BY performance_rating;

-- Top performing departments
SELECT
    d.department_name,
    ROUND(AVG(p.performance_rating), 2) AS avg_performance_rating
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN performance_reviews p ON p.employee_id = e.employee_id
GROUP BY d.department_name
ORDER BY avg_performance_rating DESC, d.department_name;

-- Attendance by department
SELECT
    d.department_name,
    ROUND(AVG(a.attendance_percentage), 2) AS avg_attendance_percentage
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN attendance_summary a ON a.employee_id = e.employee_id
GROUP BY d.department_name
ORDER BY avg_attendance_percentage DESC;

-- Salary distribution bands
SELECT
    CASE
        WHEN salary < 40000 THEN '<40K'
        WHEN salary < 60000 THEN '40K-60K'
        WHEN salary < 80000 THEN '60K-80K'
        WHEN salary < 100000 THEN '80K-100K'
        WHEN salary < 130000 THEN '100K-130K'
        ELSE '130K+'
    END AS salary_band,
    COUNT(*) AS employees
FROM employees
GROUP BY salary_band
ORDER BY MIN(salary);
