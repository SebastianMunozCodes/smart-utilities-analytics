# Dataset Inspection Notes

## What does each row represent?

Each row appears to represent electricity data for one state during one month of one year. The data includes electricity sales, customer counts, and average price values across different sectors such as residential, commercial, industrial, transportation, and total.

## What are the most important columns?

The most important columns appear to be:
- Year
- Month
- State
- Sector columns such as Residential, Commercial, Industrial, Transportation, and Total
- Sales / Megawatthours
- Customers / Count
- Price / Cents per kWh

## Which columns are categories?

Category-like columns:
- State
- Sector type, such as Residential, Commercial, Industrial, Transportation, and Total

Right now, the sector names are spread across the column headers instead of being stored in one clean `sector` column.

## Which columns are dates, years, months, or time-related?

Time-related columns:
- Year
- Month

There does not appear to be a full date column yet.

## Which columns are locations?

Location-related columns:
- State

The dataset appears to use state abbreviations such as AK, AL, and AR.

## Which columns are numeric?

Numeric columns should include:
- Year
- Month
- Sales / Megawatthours
- Customers / Count
- Price / Cents per kWh

However, Pandas currently reads all 24 columns as strings. Some numeric values contain commas, such as `545,089`, so they will need to be cleaned and converted into numbers later.

## Which columns have missing values?

The missing value output shows that almost every column has at least 1 missing value.

Examples:
- `Unnamed: 0` has 1 missing value
- `Unnamed: 1` has 2 missing values
- `Unnamed: 2` has 2 missing values
- Most sector-related columns have 1 missing value

This is probably because the dataset has messy header rows and possibly a footer note row.

## Which columns look unnecessary?

Unnecessary or messy columns include:
- `Unnamed: 0`
- `Unnamed: 1`
- `Unnamed: 2`
- Other `Unnamed` columns

These are not meaningful names. They likely exist because the CSV has multi-row headers. The actual column meanings are stored in the first two rows.

The final row also appears to contain a note rather than real data:
`For October and November 2017, Puerto Rico Ele...`

That row should probably be removed during cleaning.

## Which column represents usage, cost, consumption, emissions, or energy amount?

The energy usage / consumption column appears to be:
- `Sales`
- measured in `Megawatthours`

There is also:
- `Customers`, measured as `Count`
- `Price`, measured as `Cents/kWh`

This dataset does not appear to include emissions data.