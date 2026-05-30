# Smart Utilities Analytics

## Overview

Smart Utilities Analytics is a data analytics project that analyzes monthly electricity sales, revenue, customer count, and retail price data from the U.S. Energy Information Administration.

The project uses Python, Pandas, Matplotlib, SQLite, and SQL to clean the dataset, create summary analysis, generate charts, store the cleaned data in a database, reproduce the analysis with SQL queries, and generate a final written report.

The project demonstrates a full data workflow:

```text
Raw EIA data → cleaned CSV → Pandas analysis → charts → SQLite database → SQL analysis → generated report
```

## Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [Dataset](#dataset)
- [Dataset Files](#dataset-files)
- [Dataset Columns](#dataset-columns)
- [Tools Used](#tools-used)
- [Features](#features)
- [Project Structure](#project-structure)
- [Folder Responsibilities](#folder-responsibilities)
- [Script Responsibilities](#script-responsibilities)
- [Data Cleaning Summary](#data-cleaning-summary)
- [Pandas Analysis](#pandas-analysis)
- [Database Setup](#database-setup)
- [SQL Analysis](#sql-analysis)
- [How to Recreate the Database](#how-to-recreate-the-database)
- [How to Run](#how-to-run)
- [Example Analysis](#example-analysis)
- [Charts](#charts)
- [Generated Report](#generated-report)
- [Reports](#reports)
- [Future Improvements](#future-improvements)

## Motivation

This project was created to practice data management, data cleaning, SQL analysis, data visualization, and reporting skills using a real-world utility dataset.

The goal was to build a project that connects raw data processing with a practical utilities-style use case. Instead of only cleaning a dataset or only making charts, this project follows a complete workflow from raw data to cleaned data, analysis, database storage, SQL validation, charts, and written findings.

## Dataset

This project uses electricity sales, revenue, customer count, and retail price data from the U.S. Energy Information Administration (EIA), specifically Form EIA-861M, formerly Form EIA-826.

The dataset focuses on monthly electricity data by state and sector.

The data includes:

- Electricity sales
- Electricity revenue
- Customer counts
- Average retail electricity price
- Residential, commercial, industrial, transportation, and total sector data

The original dataset came from an Excel file and was exported to CSV format for the project.

The raw CSV had a multi-row header structure, which required cleaning before analysis.

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

Each row represents one state-year-month electricity record.

Important columns include:

- `year`
- `month`
- `state`
- `data_status`
- `residential_revenue_thousand_dollars`
- `residential_sales_megawatthours`
- `residential_customers_count`
- `residential_price_cents_kwh`
- `commercial_revenue_thousand_dollars`
- `commercial_sales_megawatthours`
- `commercial_customers_count`
- `commercial_price_cents_kwh`
- `industrial_revenue_thousand_dollars`
- `industrial_sales_megawatthours`
- `industrial_customers_count`
- `industrial_price_cents_kwh`
- `transportation_revenue_thousand_dollars`
- `transportation_sales_megawatthours`
- `transportation_customers_count`
- `transportation_price_cents_kwh`
- `total_revenue_thousand_dollars`
- `total_sales_megawatthours`
- `total_customers_count`
- `total_price_cents_kwh`

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
- Git/GitHub
- VSCode

## Features

This project can:

- Clean raw EIA electricity data.
- Handle a messy multi-row header structure.
- Standardize column names.
- Convert numeric columns into usable data types.
- Save the cleaned dataset as a CSV file.
- Generate Pandas summary analysis.
- Create charts for electricity sales, revenue, price, and monthly trends.
- Load cleaned data into a SQLite database.
- Run SQL queries that reproduce the Pandas summaries.
- Validate SQL results against Pandas findings.
- Generate a written Markdown summary report.

## Project Structure

```text
smart-utilities-analytics/
├── charts/
│   ├── top_10_states_by_total_sales.png
│   ├── top_10_states_by_average_price.png
│   ├── top_10_states_by_total_revenue.png
│   ├── average_electricity_sales_by_month.png
│   ├── top_10_records_total_sales.png
│   ├── top_10_records_total_revenue.png
│   └── top_10_records_total_price.png
├── data/
│   ├── raw/
│   └── cleaned/
├── database/
├── reports/
│   ├── cleaning_notes.md
│   ├── pandas_analysis_notes.md
│   ├── sql_analysis_notes.md
│   └── summary_report.md
├── src/
│   ├── clean_data.py
│   ├── analyze_pandas.py
│   ├── setup_database.py
│   ├── load_data.py
│   ├── analyze_sql.py
│   └── generate_report.py
├── README.md
└── requirements.txt
```

## Folder Responsibilities

| Folder | Purpose |
|---|---|
| `data/raw/` | Stores raw source files |
| `data/cleaned/` | Stores cleaned CSV output |
| `src/` | Stores Python scripts |
| `charts/` | Stores generated chart images |
| `database/` | Stores the local SQLite database |
| `reports/` | Stores analysis notes and generated reports |

## Script Responsibilities

| Script | Purpose |
|---|---|
| `src/clean_data.py` | Cleans the raw EIA dataset and saves the cleaned CSV |
| `src/analyze_pandas.py` | Creates Pandas summaries and Matplotlib charts |
| `src/setup_database.py` | Creates the SQLite database table |
| `src/load_data.py` | Loads cleaned CSV data into SQLite |
| `src/analyze_sql.py` | Runs SQL analysis queries on the SQLite database |
| `src/generate_report.py` | Generates the final Markdown summary report |

Project pipeline:

```text
clean_data.py → analyze_pandas.py → setup_database.py → load_data.py → analyze_sql.py → generate_report.py
```

## Data Cleaning Summary

The raw EIA CSV required cleaning before analysis because it had a multi-row header structure and numeric values stored as strings.

Cleaning steps included:

- Converting the original Excel dataset into CSV format.
- Identifying and handling the multi-row header structure.
- Rebuilding meaningful column names using sector and measurement labels.
- Removing non-data rows, including extra header rows and the footer note row.
- Standardizing column names.
- Removing commas from numeric values.
- Converting revenue, sales, customer count, and price columns into numeric data types.
- Converting `year` and `month` into numeric columns.
- Checking for missing values after cleaning.
- Checking for duplicate rows.
- Saving the cleaned dataset to `data/cleaned/`.

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

The Pandas analysis creates five main summaries:

- Top 10 states by total electricity sales
- Top 10 states by average electricity price
- Top 10 states by total electricity revenue
- Average electricity sales by month
- Top 10 state-year-month records ranked by total electricity sales, with revenue and price included for context

The Pandas script also generates charts and saves them in the `charts/` folder.

## Database Setup

The cleaned electricity dataset is loaded into a SQLite database.

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

The row count test confirmed that the cleaned CSV and SQLite table both contain 9,894 rows.

The `database/utilities.db` file is treated as a generated local file. It does not need to be committed to GitHub because it can be recreated from the cleaned CSV using the project scripts.

If `.gitignore` excludes database files such as `database/*.db`, the database will not appear on GitHub. This is expected. The scripts needed to recreate the database are included in the repository.

## SQL Analysis

SQL analysis is handled in:

```text
src/analyze_sql.py
```

The SQL analysis reproduces the five main Pandas summaries using SQLite queries:

- Top 10 states by total electricity sales
- Top 10 states by average electricity price
- Top 10 states by total electricity revenue
- Average electricity sales by month
- Top 10 state-year-month records ranked by total electricity sales, with revenue and price included for context

The SQL analysis confirms the same main findings as the Pandas analysis:

- Texas had the highest total electricity sales.
- Hawaii had the highest average electricity price.
- California had the highest total electricity revenue.
- Average electricity sales were highest in July and August.
- Average electricity sales were lowest in April.
- The top 10 individual state-year-month electricity sales records were all Texas summer records.

The SQL output uses custom terminal formatting, so the display order may differ slightly from the Pandas DataFrame output. However, the rankings, values, and findings match the Pandas analysis.

## How to Recreate the Database

The SQLite database can be recreated locally from the cleaned CSV.

From the project root, run:

```bash
python3 src/setup_database.py
python3 src/load_data.py
python3 src/analyze_sql.py
```

These scripts create the SQLite database, create the `electricity_sales` table, load the cleaned CSV into the table, and run SQL analysis queries.

Expected row count:

```text
9894
```

Important: `src/setup_database.py` drops and recreates the `electricity_sales` table. If it is run after loading the data, `src/load_data.py` must be run again.

## How to Run

### 1. Install dependencies

From the project root, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Clean the raw data

```bash
python3 src/clean_data.py
```

### 3. Run Pandas analysis and create charts

```bash
python3 src/analyze_pandas.py
```

### 4. Create the SQLite database table

```bash
python3 src/setup_database.py
```

### 5. Load cleaned CSV data into SQLite

```bash
python3 src/load_data.py
```

### 6. Run SQL analysis

```bash
python3 src/analyze_sql.py
```

### 7. Generate the summary report

```bash
python3 src/generate_report.py
```

Recommended full workflow:

```bash
python3 src/clean_data.py
python3 src/analyze_pandas.py
python3 src/setup_database.py
python3 src/load_data.py
python3 src/analyze_sql.py
python3 src/generate_report.py
```

## Example Analysis

The analysis found that Texas had the highest total electricity sales across the dataset, followed by California and Florida.

California had the highest total electricity revenue, followed by Texas and Florida. This shows that the state with the highest electricity sales is not necessarily the state with the highest electricity revenue.

Hawaii had the highest average electricity price, followed by Connecticut and Alaska. This shows that states with the highest average electricity prices are different from the states with the highest total electricity sales.

Average electricity sales were highest in July and August and lowest in April, suggesting higher electricity demand during summer months.

The top individual state-year-month electricity sales records were all Texas summer records, mostly from July, August, and September.

The SQL analysis reproduced the main Pandas summaries, confirming the consistency of the results across both tools.

## Charts

The project generated seven Matplotlib charts. A few key charts are shown below.

### Top 10 States by Total Electricity Sales

![Top 10 states by total electricity sales](charts/top_10_states_by_total_sales.png)

### Top 10 States by Average Electricity Price

![Top 10 states by average electricity price](charts/top_10_states_by_average_price.png)

### Average Electricity Sales by Month

![Average electricity sales by month](charts/average_electricity_sales_by_month.png)

Additional charts created:

- `charts/top_10_states_by_total_revenue.png`
- `charts/top_10_records_total_sales.png`
- `charts/top_10_records_total_revenue.png`
- `charts/top_10_records_total_price.png`

## Generated Report

A Markdown summary report can be generated with:

```bash
python3 src/generate_report.py
```

The generated report is saved to:

```text
reports/summary_report.md
```

The report summarizes the dataset, cleaning process, analysis workflow, key findings, charts, SQL validation, conclusion, and future improvements.

## Reports

Additional project notes are stored in:

- `reports/cleaning_notes.md`
- `reports/pandas_analysis_notes.md`
- `reports/sql_analysis_notes.md`
- `reports/summary_report.md`
- `reports/resume_bullets.md`

## Future Improvements

Future improvements for this project could include:

- Add sector-level analysis for residential, commercial, industrial, and transportation electricity data.
- Add more SQL queries for year-over-year comparisons.
- Create additional charts for sector-level trends.
- Build an interactive dashboard interface.
- Add automated testing for the cleaning and database-loading scripts.
- Improve chart styling and add more visualizations.
- Improve the README with chart screenshots or preview images.
- Add a final PDF report version.
- Expand the report generation script so it calculates more values dynamically instead of relying mostly on known findings.