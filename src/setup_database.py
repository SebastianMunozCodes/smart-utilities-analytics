import sqlite3

DATABASE_FILE = "database/utilities.db"

connection = sqlite3.connect(DATABASE_FILE)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS electricity_sales")

cursor.execute(""" 
CREATE TABLE electricity_sales(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               year INTEGER,
               month INTEGER,
               state TEXT,
               data_status TEXT,

               residential_revenue_thousand_dollars REAL,
               residential_sales_megawatthours REAL,
               residential_customers_count REAL,
               residential_price_cents_kwh REAL,

               commercial_revenue_thousand_dollars REAL,
               commercial_sales_megawatthours REAL,
               commercial_customers_count REAL,
               commercial_price_cents_kwh REAL,

               industrial_revenue_thousand_dollars REAL,
               industrial_sales_megawatthours REAL,
               industrial_customers_count REAL,
               industrial_price_cents_kwh REAL,

               transportation_revenue_thousand_dollars REAL,
               transportation_sales_megawatthours REAL,
               transportation_customers_count REAL,
               transportation_price_cents_kwh REAL,

               total_revenue_thousand_dollars REAL,
               total_sales_megawatthours REAL,
               total_customers_count REAL,
               total_price_cents_kwh REAL
               )
""")

connection.commit()

connection.close()

print("Database and electricity_sales table created successfully.")