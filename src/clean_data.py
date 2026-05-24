import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

RAW_FILE = "data/raw/eia_sales_revenue_monthly_states.csv"
CLEANED_FILE = "data/raw/eia_sales_revenue_monthly_states_cleaned.csv"

df = pd.read_csv(RAW_FILE)

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nSummary Statistics:")
print(df.describe())