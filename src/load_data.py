from pathlib import Path 
import sqlite3
import pandas as pd

current_dir = Path(__file__).parent
project_root = current_dir.parent
cleaned_csv_path = project_root / "data" / "cleaned" / "eia_sales_revenue_monthly_states_cleaned.csv"

database_path = project_root / "database" / "utilities.db"

df = pd.read_csv(cleaned_csv_path)

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

for row in df.itertuples():
    cursor.execute("""
        INSERT INTO electricity_sales(
            year,
            month,
            state,
            data_status,
            residential_revenue_thousand_dollars,
            residential_sales_megawatthours,
            residential_customers_count,
            residential_price_cents_kwh,
            commercial_revenue_thousand_dollars,
            commercial_sales_megawatthours,
            commercial_customers_count,
            commercial_price_cents_kwh,
            industrial_revenue_thousand_dollars,
            industrial_sales_megawatthours,
            industrial_customers_count,
            industrial_price_cents_kwh,
            transportation_revenue_thousand_dollars,
            transportation_sales_megawatthours,
            transportation_customers_count,
            transportation_price_cents_kwh,
            total_revenue_thousand_dollars,
            total_sales_megawatthours,
            total_customers_count,
            total_price_cents_kwh
        )
        VALUES(
            ?, ?, ?, ?, 
            ?, ?, ?, ?, 
            ?, ?, ?, ?, 
            ?, ?, ?, ?, 
            ?, ?, ?, ?, 
            ?, ?, ?, ?
        )
    """,(
        row.year,
        row.month,
        row.state,
        row.data_status,
        row.residential_revenue_thousand_dollars,
        row.residential_sales_megawatthours,
        row.residential_customers_count,
        row.residential_price_cents_kwh,
        row.commercial_revenue_thousand_dollars,
        row.commercial_sales_megawatthours,
        row.commercial_customers_count,
        row.commercial_price_cents_kwh,
        row.industrial_revenue_thousand_dollars,
        row.industrial_sales_megawatthours,
        row.industrial_customers_count,
        row.industrial_price_cents_kwh,
        row.transportation_revenue_thousand_dollars,
        row.transportation_sales_megawatthours,
        row.transportation_customers_count,
        row.transportation_price_cents_kwh,
        row.total_revenue_thousand_dollars,
        row.total_sales_megawatthours,
        row.total_customers_count,
        row.total_price_cents_kwh
    ))

connection.commit()

cursor.execute("SELECT COUNT(*) FROM electricity_sales")
row_count = cursor.fetchone()[0]

connection.close()

print(f"Inserted {row_count} rows into electricity_sales.")
