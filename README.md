# Smart Utilities Analytics

## Project Overview
This project analyzes utility or energy-related data using Python, CSV processing, data cleaning, SQL, and basic reporting

## Goal
The goal is to explore energy or utility usage trends and create a small analytics project that demonstrates data management skills

## Dataset
This project uses electricity sales, revenue, customer count, and retail price data from the U.S. Energy Information Administration (EIA), specifically Form EIA-861M, formerly Form EIA-826

The dataset was found through the Rutgers New Jersey Energy Data Center and focuses on monthly electricity data by state and sector

Original file format: XLSX  
Planned project format: CSV

## Dataset Columns
The raw dataset comes from EIA Form EIA-861M electricity sales/revenue data. The active sheet exported to CSV is the Monthly-States sheet.

Each row represents electricity data for one state during one month and year

Important columns:
- Year
- Month
- State
- Data Status
- Residential Revenue
- Residential Sales
- Residential Customers
- Residential Price
- Commercial Revenue
- Commercial Sales
- Commercial Customers
- Commercial Price
- Industrial Revenue
- Industrial Sales
- Industrial Customers
- Industrial Price
- Transportation Revenue
- Transportation Sales
- Transportation Customers
- Transportation Price
- Total Revenue
- Total Sales
- Total Customers
- Total Price

Possible numeric columns:
- Revenue columns: measured in thousand dollars
- Sales columns: measured in megawatthours
- Customer columns: measured as counts
- Price columns: measured in cents per kWh

Possible category columns:
- State
- Data Status
- Sector, although sector is spread across grouped columns in the raw CSV

Possible date/year columns:
- Year
- Month

Important note:
The actual data begins after the header rows, starting with rows that contain Year, Month, and State values

## Initial Dataset Notes

Dataset file:
- data/raw/eia_sales_revenue_monthly_states.csv
- Original source file: data/raw/eia_sales_revenue_original.xlsx

What each row represents:
- Each row represents monthly electricity data for one U.S. state.
- The project will focus mainly on New Jersey electricity data.

Important columns:
- Year
- Month
- State
- Data Status
- Residential Revenue, Sales, Customers, and Price
- Commercial Revenue, Sales, Customers, and Price
- Industrial Revenue, Sales, Customers, and Price
- Transportation Revenue, Sales, Customers, and Price
- Total Revenue, Sales, Customers, and Price

Numeric columns that may need conversion:
- Year
- Month
- Revenue columns
- Sales columns
- Customer count columns
- Price columns

Important conversion note:
- CSV values are read as strings first.
- Some numeric values contain commas, such as "197,690".
- These commas must be removed before converting values to int or float.

Possible questions to answer:
- How has New Jersey electricity usage changed over time?
- Which sector uses the most electricity in New Jersey?
- How does residential electricity usage compare to commercial and industrial usage?
- How has the average retail price of electricity changed over time?
- Which months have the highest total electricity sales?
- How has total electricity revenue changed over time?
- How many electricity customers are there in New Jersey over time?

## Tools Used
- Python
- CSV files
- SQLite
- SQL
- Matplotlib

## Planned Features
- Load raw CSV data
- Clean and convert data types
- Store cleaned data in a database
- Run SQL analysis
- Generate summary reports
- Create charts

## Cleaning Plan

Cleaning steps planned:
- Load and inspect the raw EIA electricity sales and revenue CSV.
- Standardize the initial column names.
- Rebuild meaningful column names from the dataset's multi-row header structure.
- Remove non-data rows, including extra header rows and the footer note row.
- Check for missing values after removing non-data rows.
- Keep useful location, time, sector, sales, customer, revenue, and price columns.
- Convert numeric columns to proper number types.
- Convert 'year' and 'month' into numeric columns.
- Check for duplicate rows.
- Save cleaned data to 'data/cleaned/'.

Specific cleaning steps for this dataset:
- Remove the first two rows that are being read as regular data but actually contain header and unit information.
- Use meaningful column names instead of 'Unnamed' columns.
- Build final column names using:
  - base columns: 'year',' 'month', 'state', 'data_status'
  - sector names: 'residential', 'commercial', 'industrial', 'transportation', and 'total'
  - measurement names: 'revenue_thousand_dollars', 'sales_megawatthours', 'customers_count', and 'price_cents_kwh'
- Keep useful time columns such as 'year' and 'month'.
- Keep the location column 'state'.
- Keep electricity sector data for residential, commercial, industrial, transportation, and total usage.
- Keep key measurement columns related to revenue, sales, customers, and price.
- Remove commas from revenue, sales, and customer count values.
- Convert revenue, sales, customer count, and price columns into numeric values.
- Convert 'year' and 'month' into numeric values.
- Remove the footer note row at the bottom of the dataset.
- Check for duplicate rows and remove them if any exist.
- Save the cleaned dataset as 'eia_sales_revenue_monthly_states_cleaned.csv' in 'data/cleaned/'.

### Column Selection Decision

At this stage, all meaningful columns are being kept. Although many columns originally appeared as 'Unnamed' columns, they were not removed immediately because the dataset used a multi-row header structure. Some of those columns contained important information such as year, month, state, data status, revenue, sales, customers, and price.

After rebuilding the column names, the dataset contains useful time, location, sector, and measurement columns. Since all of these columns may support future analysis, no major columns were removed at this stage.

### Missing Values Decision

Missing values were not filled or dropped immediately because the initial missing values appeared to come mainly from the dataset's multi-row header structure and footer note row.

The cleaning process first rebuilt the header structure, removed non-data rows, and then checked missing values again on the cleaned dataset.

After removing the extra header rows and footer note row, the important columns no longer showed missing values.

Missing values strategy:
- Rows missing 'year', 'month', or 'state' would be removed because time and location are necessary for analysis.
- Rows missing important numeric fields such as sales, customers, revenue, or price would be investigated before removal.
- Numeric values will not be filled with guesses.
- Category fields may be filled with 'Unknown' only if needed.