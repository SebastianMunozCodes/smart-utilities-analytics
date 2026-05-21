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
