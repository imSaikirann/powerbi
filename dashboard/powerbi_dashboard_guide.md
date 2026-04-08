# HR Analytics Dashboard Build Guide

## Data Source

- Primary table: `vw_hr_employee_snapshot`
- KPI view: `vw_hr_kpis`
- If PostgreSQL is unavailable, import `data/cleaned/hr_employee_data_clean.csv` into Power BI

## Pages

### 1. Executive Overview

- KPI Cards:
  - Total Employees
  - Attrition Rate %
  - Average Salary
  - Average Tenure
- Line Chart:
  - Axis: `date_of_joining` grouped by month
  - Values: `employee_id` count
  - Title: `Monthly Hiring Trend`
- Donut Chart:
  - Legend: `attrition`
  - Values: `employee_id` count
  - Title: `Attrition Distribution`
- Slicers:
  - `department`
  - `location`
  - `gender`

### 2. Workforce Performance

- Clustered Bar Chart:
  - Axis: `department`
  - Values: average `performance_rating`
  - Title: `Department-Wise Performance`
- Scatter Plot:
  - X: `attendance_percentage`
  - Y: `performance_rating`
  - Size: `salary`
  - Legend: `department`
- Matrix:
  - Rows: `department`, `job_role`
  - Values: average `performance_rating`, average `attendance_percentage`

### 3. Compensation and Attendance

- Histogram or Column Chart:
  - Axis: salary band
  - Values: employee count
  - Title: `Salary Distribution`
- Map or Filled Map:
  - Location: `location`
  - Values: employee count
- Line or Area Chart:
  - Axis: department
  - Values: average `attendance_percentage`

## Recommended DAX Measures

```DAX
Total Employees = COUNTROWS('hr_employee_data_clean')

Attrition Count = CALCULATE([Total Employees], 'hr_employee_data_clean'[attrition] = "Yes")

Attrition Rate % = DIVIDE([Attrition Count], [Total Employees], 0)

Average Salary = AVERAGE('hr_employee_data_clean'[salary])

Average Tenure = AVERAGE('hr_employee_data_clean'[tenure_years])

Average Performance = AVERAGE('hr_employee_data_clean'[performance_rating])

Average Attendance = AVERAGE('hr_employee_data_clean'[attendance_percentage])
```

## Design Notes

- Use consistent colors: teal for headcount, red for attrition, amber for attendance, blue for salary
- Add tooltips for `department`, `job_role`, and `location`
- Enable cross-filtering between charts
- Format salary values as currency and attrition as percentage
