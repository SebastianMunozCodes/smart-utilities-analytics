import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

RAW_FILE = "data/raw/eia_sales_revenue_monthly_states.csv"
CLEANED_FILE = "data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv"

df = pd.read_csv(RAW_FILE)

print("Current column names:")
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

print("\nFirst 10 rows:")
print(df.head(10).to_string())

# Rebuild meaningful column names
base_columns = ['year', 'month', 'state', 'data_status']
print("\nBase columns:")
print(base_columns)

sectors = ['residential', 'commercial', 'industrial', 'transportation', 'total']
print("\nSector columns:")
print(sectors)

measurements = ['revenue_thousand_dollars', 'sales_megawatthours', 'customers_count', 'price_cents_kwh']
print("\nMeasurement columns:")
print(measurements)

new_columns = base_columns.copy()

for i in sectors:
    for j in measurements:
        combined_name = i + "_" + j
        new_columns.append(combined_name)

print("\nNew column names:")
print(new_columns)

print("\nNumber of current DataFrame columns:")
print(len(df.columns))

print("\nNumber of new column names:")
print(len(new_columns))

print("\nLast row:")
print(df.tail(1).to_string())

df = df.drop([0, 1])
df = df.reset_index(drop=True)

df = df.iloc[:-1]
df = df.reset_index(drop=True)

df.columns = new_columns
print("\nFirst NEW 10 rows:")
print(df.head(10).to_string())

print("\nLast row:")
print(df.tail(1).to_string())

print("\nMissing values after column selection:")
print(df.isna().sum())

# Convert numeric columns
for i in df.columns[4:]:
    df[i] = df[i].astype(str).str.replace(",", "", regex=False)
    df[i] = pd.to_numeric(df[i], errors='coerce')

for i in df.columns[:2]:
    df[i] = pd.to_numeric(df[i], errors='coerce')

print("\nFirst NEW 10 rows with numeric changes:")
print(df.head(10).to_string())

print("\nLast row with numeric changes:")
print(df.tail(1).to_string())

print("\nData types:")
print(df.dtypes)