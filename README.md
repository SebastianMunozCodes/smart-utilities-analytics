# Smart Utilities Analytics

## Project Overview

This project analyzes monthly U.S. electricity sales, revenue, customer count, and retail price data using Python, Pandas, Matplotlib, SQLite, and SQL.

The project demonstrates a full data workflow:

```text
Raw EIA data → cleaned CSV → Pandas analysis → charts → SQLite database → SQL analysis
```

## Goal

The goal is to explore electricity usage, revenue, pricing, and seasonal patterns while demonstrating data cleaning, data analysis, visualization, and database querying skills.

## Dataset

This project uses electricity sales, revenue, customer count, and retail price data from the U.S. Energy Information Administration (EIA), specifically Form EIA-861M, formerly Form EIA-826.

The dataset was found through the Rutgers New Jersey Energy Data Center and focuses on monthly electricity data by state and sector.

Original file format: XLSX  
Project raw format: CSV  
Cleaned project format: CSV and SQLite database

## Dataset Files

Raw CSV:

```text
data/raw/eia_sales_revenue_monthly_states.csv
```

Cleaned CSV:

```text
data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv
```

SQLite database:

```text
database/utilities.db
```

Note: The database file may be excluded from GitHub if `.gitignore` ignores `.db` files. This is expected because the database can be recreated using the project scripts.

## Dataset Columns

Each row represents electricity data for one state during one month and year.

Important columns include:

- Year
- Month
- State
- Data Status
- Residential Revenue, Sales, Customers, and Price
- Commercial Revenue, Sales, Customers, and Price
- Industrial Revenue, Sales, Customers, and Price
- Transportation Revenue, Sales, Customers, and Price
- Total Revenue, Sales, Customers, and Price

Units:

- Revenue columns are measured in thousand dollars.
- Sales columns are measured in megawatthours.
- Customer columns are measured as counts.
- Price columns are measured in cents per kilowatthour.

## Tools Used

- Python
- Pandas
- Matplotlib
- SQLite
- SQL
- CSV files

## Features

- Load and inspect raw EIA electricity data
- Clean a messy multi-row CSV header structure
- Rebuild meaningful column names
- Convert numeric columns into usable data types
- Save cleaned data as a CSV
- Analyze electricity sales, revenue, prices, and seasonal trends with Pandas
- Generate charts with Matplotlib
- Load cleaned data into a SQLite database
- Run SQL aggregation queries
- Compare SQL results against earlier Pandas findings

## Project Structure

```text
smart-utilities-analytics/
├── charts/
├── data/
│   ├── raw/
│   └── cleaned/
├── database/
├── reports/
├── src/
│   ├── clean_data.py
│   ├── analyze_pandas.py
│   ├── setup_database.py
│   ├── load_data.py
│   └── analyze_sql.py
├── README.md
└── requirements.txt
```

## Script Responsibilities

Each script has a clear role in the project pipeline:

| Script | Purpose |
|---|---|
| `src/clean_data.py` | Cleans the raw EIA CSV and saves the cleaned CSV |
| `src/analyze_pandas.py` | Uses the cleaned CSV to create Pandas summaries and Matplotlib charts |
| `src/setup_database.py` | Creates the SQLite database table |
| `src/load_data.py` | Loads the cleaned CSV rows into the SQLite table |
| `src/analyze_sql.py` | Runs SQL analysis queries on the SQLite database |

Project pipeline:

```text
clean_data.py → analyze_pandas.py → setup_database.py → load_data.py → analyze_sql.py
```

## Data Cleaning Summary

The raw EIA CSV had a messy multi-row header structure.

The cleaning process:

- Loaded the raw CSV with Pandas
- Rebuilt meaningful column names
- Removed non-data header rows
- Removed the footer note row
- Converted year and month to numeric values
- Removed commas from numeric fields
- Converted revenue, sales, customer count, and price columns to numeric values
- Checked missing values
- Checked duplicate rows
- Saved the cleaned dataset to `data/cleaned/`

The cleaned dataset contains:

- 9,894 rows
- 24 columns
- No duplicate rows found
- No missing values in the important analysis columns

Full cleaning details are documented in:

```text
reports/cleaning_notes.md
```

## Pandas Analysis

Pandas analysis is handled in:

```text
src/analyze_pandas.py
```

Current Pandas summaries include:

- Top 10 states by total electricity sales
- Top 10 states by average electricity price
- Top 10 states by total electricity revenue
- Average electricity sales by month
- Top 10 state-year-month records ranked by total electricity sales
- Revenue and price comparisons for the top electricity sales records

## Charts

Charts are saved in the `charts/` folder.

Current charts include:

- `charts/top_10_states_by_total_sales.png`
- `charts/top_10_states_by_average_price.png`
- `charts/top_10_states_by_total_revenue.png`
- `charts/average_electricity_sales_by_month.png`
- `charts/top_10_records_total_sales.png`
- `charts/top_10_records_total_revenue.png`
- `charts/top_10_records_total_price.png`

## Database Setup

The cleaned electricity dataset was loaded into a SQLite database.

Database file:

```text
database/utilities.db
```

Main table:

```text
electricity_sales
```

The table stores monthly electricity sales, revenue, customer count, and retail price data by state and sector.

The database table is created by:

```text
src/setup_database.py
```

The cleaned CSV data is loaded into the database by:

```text
src/load_data.py
```

Initial SQL test queries include:

- Total row count
- Top states by total electricity sales

The row count test confirmed that the cleaned CSV and SQLite table both contain 9,894 rows.

An initial SQL aggregation query for total electricity sales by state matched the earlier Pandas analysis, with Texas appearing as the highest total electricity sales state.

The `database/utilities.db` file is treated as a generated local file. It does not need to be committed to GitHub because it can be recreated from the cleaned CSV using the project scripts.

If `.gitignore` excludes database files such as `database/*.db`, the database will not appear on GitHub. This is expected. The scripts needed to recreate the database are included in the repository.

## How to Recreate the Database

The SQLite database can be recreated locally from the cleaned CSV.

From the project root, run:

```bash
python3 src/setup_database.py
python3 src/load_data.py
python3 src/analyze_sql.py
```

These scripts create the SQLite database, create the `electricity_sales` table, load the cleaned CSV into the table, and run initial SQL test queries.

Expected row count:

```text
9894
```

Important: `src/setup_database.py` drops and recreates the `electricity_sales` table. If you run it after loading the data, you must run `src/load_data.py` again.

## SQL Analysis

SQL analysis is handled in:

```text
src/analyze_sql.py
```

Current SQL analysis includes:

- Counting total rows in the `electricity_sales` table
- Grouping electricity sales by state
- Ranking states by total electricity sales

The SQL result for top states by total electricity sales matched the Pandas result.

Top states by total electricity sales:

1. Texas
2. California
3. Florida
4. Ohio
5. Pennsylvania

## Early Findings

- Texas had the highest total electricity sales across the dataset.
- California had the highest total electricity revenue.
- Hawaii had the highest average electricity price.
- Average electricity sales were highest in July and August.
- Average electricity sales were lowest around April.
- The top 10 state-year-month electricity sales records were all Texas records from July, August, or September.

## How to Run the Project

### 1. Clean the raw data

```bash
python3 src/clean_data.py
```

### 2. Run Pandas analysis and create charts

```bash
python3 src/analyze_pandas.py
```

### 3. Create the SQLite database table

```bash
python3 src/setup_database.py
```

### 4. Load cleaned CSV data into SQLite

```bash
python3 src/load_data.py
```

### 5. Run SQL analysis

```bash
python3 src/analyze_sql.py
```

Important: If rebuilding the database, run the database scripts in this order:

```bash
python3 src/setup_database.py
python3 src/load_data.py
python3 src/analyze_sql.py
```

`setup_database.py` recreates the table, so running it after `load_data.py` will erase the loaded rows.

## Current Progress

Completed:

- Project folder structure created
- Raw EIA electricity dataset added
- Raw Excel file converted into CSV format
- Raw dataset inspected
- Multi-row header structure identified
- Cleaned dataset created with Pandas
- Numeric columns converted
- Duplicate rows checked
- Cleaned dataset saved
- Pandas summary analysis completed
- Seven charts created and saved
- SQLite database setup completed
- Cleaned CSV loaded into SQLite
- SQL row count verified
- SQL aggregation query matched Pandas analysis
- Analysis notes added in `reports/`

## Reports

Additional project notes are stored in:

- `reports/cleaning_notes.md`
- `reports/pandas_analysis_notes.md`

A SQL notes file may be added later as the SQL analysis phase expands.

## Next Steps

Possible future improvements:

- Add more SQL analysis queries
- Create a dedicated `reports/sql_analysis_notes.md`
- Format SQL query output more cleanly
- Add SQL queries for revenue, price, and seasonal trends
- Compare Pandas and SQL outputs in a written report
- Add more charts from SQL-based findings
- Improve README with screenshots or chart previews