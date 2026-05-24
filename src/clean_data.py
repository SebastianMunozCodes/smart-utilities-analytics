import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

RAW_FILE = "data/raw/eia_sales_revenue_monthly_states.csv"
CLEANED_FILE = "data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv"

df = pd.read_csv(RAW_FILE)

print("\nCurrent column names:")
print(df.columns.tolist())

print("\nFirst 10 rows:")
print(df.head(10).to_string())

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.replace("/", "_", regex=False)
)

print("\nCleaned column names:")
print(df.columns.tolist())

print("\nMissing values after column selection:")
print(df.isna().sum())

print("-" * 100)

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nSummary Statistics:")
print(df.describe())
