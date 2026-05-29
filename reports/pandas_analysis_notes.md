## Pandas Summary Analysis

Using the cleaned EIA electricity sales and revenue dataset, I created five initial Pandas summaries.

Summaries created:
- Top 10 states by total electricity sales.
- Top 10 states by average electricity price.
- Top 10 states by total electricity revenue.
- Average electricity sales by month.
- Top 10 state-year-month records ranked by total electricity sales, with total revenue and total price included for context.

These summaries use Pandas operations such as:
- `groupby()`
- `sum()`
- `mean()`
- `sort_values()`
- `sort_index()`
- `head()`
- row-level sorting

The summaries show both location-based and time-based patterns. The state-based summaries compare electricity sales, prices, and revenue across states. The monthly summary shows how average electricity sales change by month. The row-level summary identifies the specific state-year-month records with the highest total electricity sales.

Key early observations:
- Texas had the highest total electricity sales across the dataset.
- Hawaii had the highest average electricity price.
- California had the highest total electricity revenue.
- Average electricity sales were highest during the summer months, especially July and August.
- The highest individual electricity sales records were Texas summer records.

## Summaries Created

Using the cleaned EIA electricity dataset, I created five Pandas summary outputs:

1. Top 10 states by total electricity sales.
2. Top 10 states by average electricity price.
3. Top 10 states by total electricity revenue.
4. Average electricity sales by month.
5. Top 10 state-year-month records ranked by total electricity sales, with revenue and price included for context.

## Charts Created

The following charts were created and saved in the `charts/` folder:

- `charts/top_10_states_by_total_sales.png`
- `charts/top_10_states_by_average_price.png`
- `charts/top_10_states_by_total_revenue.png`
- `charts/average_electricity_sales_by_month.png`
- `charts/top_10_records_total_sales.png`
- `charts/top_10_records_total_revenue.png`
- `charts/top_10_records_total_price.png`

## Early Findings

Initial Pandas analysis shows that total electricity sales, electricity revenue, and electricity prices vary significantly by state and month.

Texas had the highest total electricity sales across the dataset, followed by California and Florida. California had the highest total electricity revenue, followed by Texas and Florida. This suggests that the state with the highest electricity sales is not necessarily the state with the highest electricity revenue.

Hawaii had the highest average electricity price, followed by Connecticut and Alaska. This shows that states with the highest electricity prices are different from the states with the highest total electricity sales.

Average electricity sales were highest during the summer months, especially July and August. The lowest average electricity sales occurred in April. This suggests a seasonal pattern where electricity demand rises during the summer.

The top 10 individual state-year-month electricity sales records were all from Texas, mostly during July, August, and September. This supports the idea that Texas has especially high electricity demand during summer months.

## SQL Comparison Update

The SQL analysis now reproduces the main Pandas summaries using SQLite queries. The SQL outputs confirm the same major findings as the Pandas analysis, including Texas having the highest total electricity sales, Hawaii having the highest average electricity price, California having the highest total electricity revenue, summer months having the highest average sales, and Texas summer records making up the top individual sales records. 
