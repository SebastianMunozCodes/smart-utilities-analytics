from pathlib import Path 
import sqlite3

current_dir = Path(__file__).parent
project_root = current_dir.parent
database_path = project_root / "database" / "utilities.db" 

connection = sqlite3.connect(database_path)
cursor = connection.cursor()



cursor.execute("SELECT COUNT(*) FROM electricity_sales")
row_count = cursor.fetchone()[0]

print(f"Rows in electricity_sales: {row_count}")

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

# Query 1: Total electricity sales by state

cursor.execute("""
    SELECT state, SUM(total_sales_megawatthours) AS total_sales_megawatthours_sum
    FROM electricity_sales
    GROUP BY state
    ORDER BY total_sales_megawatthours_sum DESC
    LIMIT 10
""")

results = cursor.fetchall()

print("\nTop 10 states by total electricity sales:")
print(f"{'Rank':<6}{'State':<8}{'Total Sales (MWh)':>22}")
print("-" * 36)

for rank, (state, total_sales) in enumerate(results, start=1):
    print(f"{rank:<6}{state:<8}{total_sales:>22,.0f}")

# Query 2: Top 10 states by average electricity price

cursor.execute("""
    SELECT state, AVG(total_price_cents_kwh) as total_price_cents_kwh_avg
    FROM electricity_sales
    GROUP BY state
    ORDER BY total_price_cents_kwh_avg DESC
    LIMIT 10
""")

results = cursor.fetchall()

print("\nTop 10 states by average electricity price:")
print(f"{'Rank':<6}{'State':<8}{'Avg Price (cents/kWh)':>24}")
print("-" * 38)

for rank, (state, avg_price) in enumerate(results, start=1):
    print(f"{rank:<6}{state:<8}{avg_price:>24.2f}")

# Query 3: Top 10 states by total electricity revenue

cursor.execute("""
    SELECT state, SUM(total_revenue_thousand_dollars) AS total_revenue_thousand_dollars_sum
    FROM electricity_sales
    GROUP BY state
    ORDER BY total_revenue_thousand_dollars_sum DESC
    LIMIT 10
""")

results = cursor.fetchall()

print("\nTop 10 states by total electricity revenue:")
print(f"{'Rank':<6}{'State':<8}{'Total Revenue (Thousand $)':>24}")
print("-" * 40)

for rank, (state, total_revenue) in enumerate(results, start=1):
    print(f"{rank:<6}{state:<8}{total_revenue:>26,.0f}")

# Query 4: Average electricity sales by month

cursor.execute("""
    SELECT month, AVG(total_sales_megawatthours) AS total_sales_megawatthours_avg
    FROM electricity_sales
    GROUP BY month 
    ORDER BY month ASC
""")

results = cursor.fetchall()

print("\nAverage electricity sales by month:")
print(f"{'Month':<8}{'Avg Sales (MWh)':>24}")
print("-" * 32)

for month, avg_sales in results:
    month_label = month_names[month]
    print(f"{month_label:<6}{avg_sales:>26,.0f}")

# Query 5: Top 10 state-year-month records ranked by total electricity sales, with revenue and price

cursor.execute("""
    SELECT state, year, month, 
           total_sales_megawatthours, 
           total_revenue_thousand_dollars, 
           total_price_cents_kwh 
    FROM electricity_sales
    ORDER BY total_sales_megawatthours DESC
    LIMIT 10
""")

results = cursor.fetchall()

print("\nTop 10 state-year-month records ranked by total electricity sales, with revenue and price:")
print(
    f"{'Rank':<6}"
    f"{'State':<8}"
    f"{'Year':<8}"
    f"{'Month':<8}"
    f"{'Total Sales (MWh)':>24}"
    f"{'Total Revenue (Thousand $)':>28}"
    f"{'Total Price (Cents/kWh)':>28}"
    f"{'Record':>18}"
)
print("-" * 128)

for rank, (state, year, month, total_sales, total_revenue, total_price) in enumerate(results, start=1):
    month_label = month_names[month]
    record = f"{state}-{year}-{month_label}"

    print(
        f"{rank:<6}"
        f"{state:<8}"
        f"{year:<8}"
        f"{month_label:<8}"
        f"{total_sales:>24,.0f}"
        f"{total_revenue:>28,.0f}"
        f"{total_price:>28.2f}"
        f"{record:>18}"
    )

connection.close()