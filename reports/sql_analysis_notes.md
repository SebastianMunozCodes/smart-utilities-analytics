# SQL Setup Notes

The cleaned EIA electricity dataset was loaded into a SQLite database.

## Database Created

`database/utilities.db`

## Main Table Created

`electricity_sales`

The table stores cleaned monthly electricity data by state, including electricity sales, revenue, customer counts, and retail price data across residential, commercial, industrial, transportation, and total sectors.

## Database Scripts

The SQLite table is created by:

`src/setup_database.py`

The cleaned CSV data is loaded into the table by:

`src/load_data.py`

SQL analysis queries are run from:

`src/analyze_sql.py`

## Row Count Test

The first SQL test query counted the number of rows in the table:

```sql
SELECT COUNT(*)
FROM electricity_sales;
```

The query returned:

```text
9894
```

This matched the number of rows in the cleaned CSV file.

## Initial SQL Aggregation Query

A second SQL test query grouped records by state and calculated total electricity sales:

```sql
SELECT state, SUM(total_sales_megawatthours) AS total_sales_megawatthours_sum
FROM electricity_sales
GROUP BY state
ORDER BY total_sales_megawatthours_sum DESC
LIMIT 10;
```

## SQL Findings

The SQL query confirmed that Texas had the highest total electricity sales.

The top 10 states by total electricity sales were:

1. Texas
2. California
3. Florida
4. Ohio
5. Pennsylvania
6. New York
7. Georgia
8. Illinois
9. North Carolina
10. Virginia

This matched the earlier Pandas analysis for top states by total electricity sales.

## Recreating the Database

The database file `database/utilities.db` is treated as a generated local file and is ignored by Git through `.gitignore`.

The database can be recreated by running these commands from the project root:

```bash
python3 src/setup_database.py
python3 src/load_data.py
python3 src/analyze_sql.py
```

Important: `src/setup_database.py` drops and recreates the `electricity_sales` table. If it is run after loading the data, `src/load_data.py` must be run again.