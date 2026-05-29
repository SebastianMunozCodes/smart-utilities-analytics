import pandas as pd
import matplotlib.pyplot as plt

CLEANED_FILE = "data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv"

df = pd.read_csv(CLEANED_FILE)

print("Cleaned data set loaded.")
print(f"Shape: {df.shape}")

# Month number labels used for display tables and charts
month_names = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

# Summary 1: Total electricity sales by state

total_sales_by_state = (
    df.groupby("state")["total_sales_megawatthours"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    )

top_10_sales_by_state = total_sales_by_state.head(10).copy()
top_10_sales_by_state.index = range(1, len(top_10_sales_by_state) + 1)

top_10_sales_by_state_display = top_10_sales_by_state.rename(
    columns={
        "state": "State",
        "total_sales_megawatthours": "Total Sales (MWh)"
    }
)

print("\nTop 10 states by total electricity sales:")
print(top_10_sales_by_state_display)

# Chart 1: Top 10 states by total electricity sales

top_10_sales_chart = top_10_sales_by_state_display.copy()

top_10_sales_chart["Total Sales (Billions of MWh)"] = (
    top_10_sales_chart["Total Sales (MWh)"] / 1_000_000_000
)

ax = top_10_sales_chart.plot(
    x="State",
    y="Total Sales (Billions of MWh)",
    kind="bar",
    figsize=(10, 6),
    legend=False
)

plt.title("Top 10 States by Total Electricity Sales")
plt.xlabel("State")
plt.ylabel("Total Sales (Billions of MWh)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}B",
        ha="center",
        va="bottom"
    )

plt.ylim(0, top_10_sales_chart["Total Sales (Billions of MWh)"].max() * 1.12)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("charts/top_10_states_by_total_sales.png")
plt.close()

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
        "total_price_cents_kwh": "Average Price (Cents/kWh)"
    }
)

print("\nTop 10 states by average electricity price:")
print(top_10_average_prices_by_state_display)

# Chart 2: Top 10 states by average electricity price

ax = top_10_average_prices_by_state_display.plot(
    x="State",
    y="Average Price (Cents/kWh)",
    kind="bar",
    figsize=(10, 6),
    legend=False
)

plt.title("Top 10 States by Average Electricity Price")
plt.xlabel("State")
plt.ylabel("Average Price (Cents/kWh)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.ylim(0, top_10_average_prices_by_state_display["Average Price (Cents/kWh)"].max() * 1.12)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("charts/top_10_states_by_average_price.png")
plt.close()

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

# Chart 3: Top 10 states by total electricity revenue

top_10_revenue_chart = top_10_revenue_by_state_display.copy()

top_10_revenue_chart["Total Revenue (Billions of $)"] = (
    top_10_revenue_chart["Total Revenue (Thousand $)"] / 1_000_000
)

ax = top_10_revenue_chart.plot(
    x="State",
    y="Total Revenue (Billions of $)",
    kind="bar",
    figsize=(10, 6),
    legend=False
)

plt.title("Top 10 States by Total Electricity Revenue")
plt.xlabel("State")
plt.ylabel("Total Revenue (Billions of $)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"${height:.1f}B",
        ha="center",
        va="bottom"
    )

plt.ylim(0, top_10_revenue_chart["Total Revenue (Billions of $)"].max() * 1.12)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("charts/top_10_states_by_total_revenue.png")
plt.close()

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

fixed_avg_sales_by_month_display["Month"] = (
    fixed_avg_sales_by_month_display["Month"].map(month_names)
)

print("\nAverage electricity sales by month:")
print(fixed_avg_sales_by_month_display)

# Chart 4: Average electricity sales by month

avg_sales_month_chart = fixed_avg_sales_by_month_display.copy()

avg_sales_month_chart["Average Sales (Millions of MWh)"] = (
    avg_sales_month_chart["Average Sales (MWh)"] / 1_000_000
)

ax = avg_sales_month_chart.plot(
    x="Month",
    y="Average Sales (Millions of MWh)",
    kind="line",
    marker="o",
    figsize=(10, 6),
    legend=False
)

plt.title("Average Electricity Sales by Month")
plt.xlabel("Month")
plt.ylabel("Average Sales (Millions of MWh)")

plt.xticks(
    ticks=range(len(avg_sales_month_chart["Month"])),
    labels=avg_sales_month_chart["Month"],
    rotation=0
)

# Find highest and lowest monthly average sales
max_index = avg_sales_month_chart["Average Sales (Millions of MWh)"].idxmax()
min_index = avg_sales_month_chart["Average Sales (Millions of MWh)"].idxmin()

max_month = avg_sales_month_chart.loc[max_index, "Month"]
max_value = avg_sales_month_chart.loc[max_index, "Average Sales (Millions of MWh)"]

min_month = avg_sales_month_chart.loc[min_index, "Month"]
min_value = avg_sales_month_chart.loc[min_index, "Average Sales (Millions of MWh)"]

# Label highest point
ax.annotate(
    f"High: {max_month} {max_value:.2f}M",
    xy=(max_index, max_value),
    xytext=(-45, 10),
    textcoords="offset points",
    ha="right",
    va="bottom"
)

# Label lowest point
ax.text(
    min_index,
    min_value,
    f"Low: {min_month} {min_value:.2f}M",
    ha="center",
    va="top"
)

plt.ylim(
    avg_sales_month_chart["Average Sales (Millions of MWh)"].min() * 0.95,
    avg_sales_month_chart["Average Sales (Millions of MWh)"].max() * 1.10
)

plt.tight_layout()

plt.savefig("charts/average_electricity_sales_by_month.png")
plt.close()

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
        "total_sales_megawatthours",
        "total_revenue_thousand_dollars",
        "total_price_cents_kwh"
    ]
].copy()

top_10_usage_records_display = top_10_usage_records_display.rename(
    columns={
        "state": "State",
        "year": "Year",
        "month": "Month",
        "total_sales_megawatthours": "Total Sales (MWh)",
        "total_revenue_thousand_dollars": "Total Revenue (Thousand $)",
        "total_price_cents_kwh": "Total Price (Cents/kWh)"
    }
)

top_10_usage_records_display["Month"] = (
    top_10_usage_records_display["Month"].map(month_names)
)

top_10_usage_records_display["Record"] = (
    top_10_usage_records_display["State"] + "-" +
    top_10_usage_records_display["Year"].astype(str) + "-" +
    top_10_usage_records_display["Month"]
)

top_10_usage_records_display.index = range(1, len(top_10_usage_records_display) + 1)

print("\nTop 10 state-year-month records ranked by total electricity sales, with revenue and price:")
print(top_10_usage_records_display)


# Chart 5A: Total sales for top 10 state-year-month records

top_10_records_sales_chart = top_10_usage_records_display.copy()

top_10_records_sales_chart["Total Sales (Millions of MWh)"] = (
    top_10_records_sales_chart["Total Sales (MWh)"] / 1_000_000
)

ax = top_10_records_sales_chart.plot(
    x="Record",
    y="Total Sales (Millions of MWh)",
    kind="bar",
    figsize=(11, 6),
    legend=False
)

plt.title("Top 10 State-Year-Month Records by Total Electricity Sales")
plt.xlabel("State-Year-Month")
plt.ylabel("Total Sales (Millions of MWh)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.1f}M",
        ha="center",
        va="bottom"
    )

plt.ylim(
    0,
    top_10_records_sales_chart["Total Sales (Millions of MWh)"].max() * 1.12
)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("charts/top_10_records_total_sales.png")
plt.close()


# Chart 5B: Revenue for top 10 electricity sales records

top_10_records_revenue_chart = top_10_usage_records_display.copy()

top_10_records_revenue_chart["Total Revenue (Billions of $)"] = (
    top_10_records_revenue_chart["Total Revenue (Thousand $)"] / 1_000_000
)

ax = top_10_records_revenue_chart.plot(
    x="Record",
    y="Total Revenue (Billions of $)",
    kind="bar",
    figsize=(11, 6),
    legend=False
)

plt.title("Revenue for Top 10 Electricity Sales Records")
plt.xlabel("State-Year-Month")
plt.ylabel("Total Revenue (Billions of $)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"${height:.1f}B",
        ha="center",
        va="bottom"
    )

plt.ylim(
    0,
    top_10_records_revenue_chart["Total Revenue (Billions of $)"].max() * 1.12
)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("charts/top_10_records_total_revenue.png")
plt.close()


# Chart 5C: Price for top 10 electricity sales records

top_10_records_price_chart = top_10_usage_records_display.copy()

ax = top_10_records_price_chart.plot(
    x="Record",
    y="Total Price (Cents/kWh)",
    kind="bar",
    figsize=(11, 6),
    legend=False
)

plt.title("Price for Top 10 Electricity Sales Records")
plt.xlabel("State-Year-Month")
plt.ylabel("Total Price (Cents/kWh)")

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.ylim(
    0,
    top_10_records_price_chart["Total Price (Cents/kWh)"].max() * 1.12
)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("charts/top_10_records_total_price.png")
plt.close()

print("\nPandas analysis complete. Charts saved to charts/.")