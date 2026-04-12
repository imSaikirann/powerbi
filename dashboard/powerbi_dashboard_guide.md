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

### 4. Data Quality Report

- KPI Cards:
  - Input Rows
  - Clean Rows
  - Duplicates Removed
  - Missing Values After Cleaning
- Table:
  - Columns: field name, null count, null percentage, status
  - Title: `Field-Level Data Quality Summary`
- Bar Chart:
  - Axis: `department`
  - Values: missing value count or corrected record count
  - Title: `Department-Wise Data Quality Impact`
- Donut Chart:
  - Legend: quality issue type
  - Values: issue count
  - Title: `Quality Issue Distribution`

### 5. Final Output Report

- KPI Cards:
  - Total Employees
  - Attrition Count
  - High Performers
  - Average Attendance
- Detailed Table:
  - Columns: `employee_id`, `department`, `job_role`, `salary`, `attendance_percentage`, `performance_rating`, `attrition`
  - Title: `Final Employee Output Summary`
- Bar Chart:
  - Axis: `department`
  - Values: employee count
  - Title: `Final Output by Department`
- Export Note:
  - Use this page as the final review page before exporting the report or dashboard screenshots

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

## DAX Reference for Overview and Performance

The following expressions are useful when building Power BI pages for executive overview and workforce performance analysis. Each item is explained one by one in simple terms.

### 1. `SUM()`

Adds all values in a numeric column.

```DAX
Total Salary Paid = SUM('hr_employee_data_clean'[salary])
```

### 2. `COUNT()`

Counts numeric values in a column. This is useful when the selected column always contains numbers.

```DAX
Employee ID Count = COUNT('hr_employee_data_clean'[employee_id])
```

### 3. `COUNTA()`

Counts all non-empty values in a column.

```DAX
Filled Job Roles = COUNTA('hr_employee_data_clean'[job_role])
```

### 4. `DISTINCTCOUNT()`

Counts unique values. This is useful for finding how many distinct departments, roles, or locations exist.

```DAX
Unique Departments = DISTINCTCOUNT('hr_employee_data_clean'[department])
```

### 5. `AVERAGE()`

Returns the average of a numeric column.

```DAX
Average Salary = AVERAGE('hr_employee_data_clean'[salary])
```

```DAX
Average Attendance = AVERAGE('hr_employee_data_clean'[attendance_percentage])
```

### 6. `MAX()` and `MIN()`

Returns the highest and lowest values from a numeric column.

```DAX
Highest Salary = MAX('hr_employee_data_clean'[salary])
Lowest Salary = MIN('hr_employee_data_clean'[salary])
```

### 7. `CALCULATE()`

Changes the filter context of a measure. This is one of the most important DAX functions in Power BI.

```DAX
Attrition Count = CALCULATE(
    [Total Employees],
    'hr_employee_data_clean'[attrition] = "Yes"
)
```

### 8. `FILTER()`

Creates a filtered table inside a calculation. It is helpful for custom business conditions.

```DAX
High Performers = CALCULATE(
    [Total Employees],
    FILTER('hr_employee_data_clean', 'hr_employee_data_clean'[performance_rating] >= 4)
)
```

### 9. `IF()`

Applies simple conditional logic and returns one result if a condition is true and another if false.

```DAX
Performance Status = IF([Average Performance] >= 4, "Strong", "Needs Attention")
```

### 10. `DIVIDE()`

Performs safe division and avoids divide-by-zero errors.

```DAX
Attrition Rate % = DIVIDE([Attrition Count], [Total Employees], 0)
```

### 11. `RELATED()`

Pulls a value from another related table. Use this when your data model contains multiple linked tables.

```DAX
Department Name = RELATED('department_lookup'[department_name])
```

### 12. `DATEADD()`

Shifts a date range forward or backward. It is useful for month-over-month or year-over-year comparisons.

```DAX
Previous Month Hires = CALCULATE(
    [Total Employees],
    DATEADD('Date'[Date], -1, MONTH)
)
```

### 13. `TOTALYTD()`

Returns the year-to-date value for a measure.

```DAX
YTD Hires = TOTALYTD([Total Employees], 'Date'[Date])
```

### 14. `SAMEPERIODLASTYEAR()`

Compares the current period with the same period in the previous year.

```DAX
Last Year Hires = CALCULATE(
    [Total Employees],
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

### 15. `SWITCH()`

Checks multiple conditions in a cleaner way than nested `IF()` functions.

```DAX
Attendance Band = SWITCH(
    TRUE(),
    [Average Attendance] >= 90, "Excellent",
    [Average Attendance] >= 75, "Good",
    "Low"
)
```

## Most Useful Dashboard Measures

These measures are the most useful for an HR dashboard overview page and performance page.

```DAX
Total Employees = COUNTROWS('hr_employee_data_clean')

Attrition Count = CALCULATE(
    [Total Employees],
    'hr_employee_data_clean'[attrition] = "Yes"
)

Attrition Rate % = DIVIDE([Attrition Count], [Total Employees], 0)

Average Salary = AVERAGE('hr_employee_data_clean'[salary])

Average Tenure = AVERAGE('hr_employee_data_clean'[tenure_years])

Average Performance = AVERAGE('hr_employee_data_clean'[performance_rating])

Average Attendance = AVERAGE('hr_employee_data_clean'[attendance_percentage])

High Performers = CALCULATE(
    [Total Employees],
    FILTER('hr_employee_data_clean', 'hr_employee_data_clean'[performance_rating] >= 4)
)

Input Rows = COUNTROWS('hr_employee_data_raw')

Clean Rows = COUNTROWS('hr_employee_data_clean')

Duplicates Removed = [Input Rows] - [Clean Rows]
```

## Growth Measure Example

Use the following pattern when you want to compare current results with a previous period.

```DAX
Growth % = DIVIDE([Total Employees] - [Last Year Hires], [Last Year Hires], 0)
```

## Design Notes

- Use consistent colors: teal for headcount, red for attrition, amber for attendance, blue for salary
- Add tooltips for `department`, `job_role`, and `location`
- Enable cross-filtering between charts
- Format salary values as currency and attrition as percentage
