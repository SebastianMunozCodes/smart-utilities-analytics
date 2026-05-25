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