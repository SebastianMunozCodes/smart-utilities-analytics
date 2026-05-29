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

cursor.execute("""
    SELECT state, SUM(total_sales_megawatthours) AS total_sales_megawatthours_sum
    FROM electricity_sales
    GROUP BY state
    ORDER BY total_sales_megawatthours_sum DESC
    LIMIT 10
""")

results = cursor.fetchall()

print(f"\nTop 10 states by total electricity sales:")

for row in results:
    print(row)

connection.close()