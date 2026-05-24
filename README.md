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
- Standardize column names
- Remove unnecessary columns
- Check for missing values
- Convert numeric columns to proper number types
- Keep useful location and time columns
- Save cleaned data to 'data/cleaned/'

Specific cleaning steps for this dataset:
- Remove extra header rows that are being read as regular data
- Use meaningful column names instead of 'Unnamed' columns
- Rename columns to lowercase with underscores
- Keep useful time columns such as year and month
- Keep the location column for state
- Keep electricity sector data such as residential, commercial, industrial, transportation, and total
- Keep key measurement columns related to sales, customers, and price
- Convert sales values from text with commas into numeric values
- Convert customer counts from text with commas into numeric values
- Convert price values into numeric decimals
- Remove the footer note row at the bottom of the dataset
- Save the cleaned dataset as 'utility_usage_cleaned.csv' in 'data/cleaned/'

### Column Selection Decision
At this stage, all columns will be kept temporaroly. Although many columns currently apeear as 'unamed' columns, they should not be removed yet becuase this data set has multi-row reader. Some of these columns contain important information such as year, month, state, data status, sales, customers, and price.

The column selection step will be revisited after the header rows are cleaned and meaningful column names are created. This avoids accidentally deleting useful data before the dataset structure is fully understood.