# SQL Analysis Notes

## Purpose

The purpose of this SQL analysis was to reproduce the five main Pandas summaries using SQLite.

Earlier in the project, the cleaned EIA electricity dataset was analyzed with Pandas. The SQL analysis uses the same cleaned data, loaded into a SQLite table, to confirm that the same major findings appear when using SQL queries.

This helps verify that the project results are consistent across both Pandas DataFrame operations and SQL database queries.

## Database Used

Database file:

```text
database/utilities.db
```

Main table:

```text
electricity_sales
```

The `electricity_sales` table stores monthly electricity sales, revenue, customer count, and retail price data by state and sector.

## Queries Created

The SQL analysis reproduces the five main Pandas summaries:

1. Top 10 states by total electricity sales
2. Top 10 states by average electricity price
3. Top 10 states by total electricity revenue
4. Average electricity sales by month
5. Top 10 state-year-month records ranked by total electricity sales, with revenue and price included for context

## Query 1: Top 10 States by Total Electricity Sales

This query groups the data by state and calculates the total electricity sales for each state using `SUM(total_sales_megawatthours)`.

SQL tools used:

- `SELECT`
- `SUM`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

The result shows which states had the highest total electricity sales across the dataset.

The SQL result matched the earlier Pandas analysis. Texas had the highest total electricity sales, followed by California and Florida.

## Query 2: Top 10 States by Average Electricity Price

This query groups the data by state and calculates the average electricity price for each state using `AVG(total_price_cents_kwh)`.

SQL tools used:

- `SELECT`
- `AVG`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

The result shows which states had the highest average electricity prices across the dataset.

The SQL result matched the earlier Pandas analysis. Hawaii had the highest average electricity price, followed by Connecticut and Alaska.

## Query 3: Top 10 States by Total Electricity Revenue

This query groups the data by state and calculates the total electricity revenue for each state using `SUM(total_revenue_thousand_dollars)`.

SQL tools used:

- `SELECT`
- `SUM`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

The result shows which states had the highest total electricity revenue across the dataset.

The SQL result matched the earlier Pandas analysis. California had the highest total electricity revenue, followed by Texas and Florida.

## Query 4: Average Electricity Sales by Month

This query groups the data by month and calculates the average electricity sales for each month using `AVG(total_sales_megawatthours)`.

SQL tools used:

- `SELECT`
- `AVG`
- `GROUP BY`
- `ORDER BY`

The query sorts by month number so the results appear in calendar order from January through December.

The SQL result matched the earlier Pandas analysis. Average electricity sales were highest during July and August, while April had the lowest average electricity sales.

This supports the finding that electricity demand follows a seasonal pattern, with higher demand during the summer months.

## Query 5: Top 10 State-Year-Month Records by Total Electricity Sales

This query selects individual state-year-month records and sorts them by `total_sales_megawatthours` from highest to lowest.

SQL tools used:

- `SELECT`
- `ORDER BY`
- `LIMIT`

Unlike the first four queries, this query does not use `GROUP BY`. It is a row-level query that returns the individual monthly records with the highest electricity sales.

The query includes:

- State
- Year
- Month
- Total sales
- Total revenue
- Total price
- A combined record label

The SQL output displays total sales before total revenue because the records are ranked by total electricity sales. This differs slightly from the Pandas display order, but the records, values, and findings match.

The SQL result matched the earlier Pandas analysis. The top 10 individual state-year-month electricity sales records were all Texas records from summer months, mostly July, August, and September.

## Overall SQL Findings

The SQL analysis reproduced the main Pandas findings:

- Texas had the highest total electricity sales.
- Hawaii had the highest average electricity price.
- California had the highest total electricity revenue.
- Average electricity sales were highest in July and August.
- The highest individual monthly electricity sales records were Texas summer records.

## Conclusion

The SQL analysis confirmed the same main findings as the Pandas analysis.

This strengthens the project because the same cleaned dataset was analyzed in two different ways:

```text
Pandas DataFrame operations
SQLite SQL queries
```

Both approaches produced matching rankings, values, and conclusions.