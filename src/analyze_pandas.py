import pandas as pd
import matplotlib.pyplot as plt

CLEANED_FILE = "data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv"

df = pd.read_csv(CLEANED_FILE)

print("Cleaned data set loaded.")
print(f"Shape: {df.shape}")

# Summary 1: Total electricity sales by state

total_sales_megawatthours = (
    df.groupby("state")["total_sales_megawatthours"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    )

top_10_sales_by_state = total_sales_megawatthours.head(10).copy()
top_10_sales_by_state.index = range(1, len(top_10_sales_by_state) + 1)

top_10_sales_by_state_display = top_10_sales_by_state.rename(
    columns={
        "state": "State",
        "total_sales_megawatthours": "Total Sales (MWh)"
    }
)

print("\nTop 10 states by total electricity sales:")
print(top_10_sales_by_state_display)

# Summary 2: Average electricity price by state

avg_price_by_state = (
    df.groupby("state")["total_price_cents_kwh"]
    .mean().sort_values(ascending=False)
    .reset_index()
)

top_10_average_prices_by_state = avg_price_by_state.head(10).copy()
top_10_average_prices_by_state.index = range(1, len(top_10_average_prices_by_state) + 1)

top_10_average_prices_by_state["total_price_cents_kwh"] = (
    top_10_average_prices_by_state["total_price_cents_kwh"].round(2)
)

top_10_average_prices_by_state_display = top_10_average_prices_by_state.rename(
    columns={
        "state": "State",
        "total_price_cents_kwh": "Average Price (Cents/kwh)"
    }
)

print("\nTop 10 states by average electricity price:")
print(top_10_average_prices_by_state_display)

# Summary 3: Total electricity revenue by state

total_revenue_by_state = (
    df.groupby("state")["total_revenue_thousand_dollars"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_10_revenue_by_state = total_revenue_by_state.head(10).copy()
top_10_revenue_by_state.index = range(1, len(top_10_revenue_by_state) + 1)

top_10_revenue_by_state_display = top_10_revenue_by_state.rename(
    columns={
        "state": "State",
        "total_revenue_thousand_dollars": "Total Revenue (Thousand $)"
    }
)

print("\nTop 10 states by total electricity revenue:")
print(top_10_revenue_by_state_display)

# Summary 4: Average electricity sales by month

avg_sales_by_month = (
    df.groupby("month")["total_sales_megawatthours"]
    .mean()
    .sort_index(ascending=True)
    .reset_index()
)

fixed_avg_sales_by_month = avg_sales_by_month.copy()
fixed_avg_sales_by_month.index = range(1, len(fixed_avg_sales_by_month) + 1)

fixed_avg_sales_by_month["total_sales_megawatthours"] = (
    fixed_avg_sales_by_month["total_sales_megawatthours"].round(0).astype(int)
)

fixed_avg_sales_by_month_display = fixed_avg_sales_by_month.rename(
    columns={
        "month": "Month",
        "total_sales_megawatthours": "Average Sales (MWh)"
    }
)

print("\nAverage electricity sales by month:")
print(fixed_avg_sales_by_month_display)

# Summary 5: Top 10 state-year-month records ranked by total electricity sales

top_10_usage_records = df.sort_values(
    by="total_sales_megawatthours",
    ascending=False
).head(10)

top_10_usage_records_display = top_10_usage_records[
    [
        "state",
        "year",
        "month",
        "total_revenue_thousand_dollars",
        "total_sales_megawatthours",
        "total_price_cents_kwh"
    ]
].copy()

top_10_usage_records_display = top_10_usage_records_display.rename(
    columns={
        "state": "State",
        "year": "Year",
        "month": "Month",
        "total_revenue_thousand_dollars": "Total Revenue (Thousand $)",
        "total_sales_megawatthours": "Total Sales (MWh)",
        "total_price_cents_kwh": "Total Price (Cents/kWh)"
    }
)

top_10_usage_records_display.index = range(1, len(top_10_usage_records_display) + 1)

print("\nTop 10 state-year-month records ranked by total electricity sales, with revenue and price:")
print(top_10_usage_records_display)
