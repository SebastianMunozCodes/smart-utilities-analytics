import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

RAW_FILE = "data/raw/eia_sales_revenue_monthly_states.csv"
CLEANED_FILE = "data/cleaned/eia_sales_revenue_monthly_states_cleaned.csv"

# Load raw data
df = pd.read_csv(RAW_FILE)

print("Raw data loaded.")
print(f"Initial shape: {df.shape}")

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

print("\nInitial column names standardized.")

# Rebuild meaningful column names
base_columns = ['year', 'month', 'state', 'data_status']

sectors = ['residential', 
           'commercial', 
           'industrial', 
           'transportation', 
           'total']

measurements = ['revenue_thousand_dollars', 
                'sales_megawatthours', 
                'customers_count', 
                'price_cents_kwh']

new_columns = base_columns.copy()

for sector in sectors:
    for measurement in measurements:
        combined_name = sector + "_" + measurement
        new_columns.append(combined_name)

if len(df.columns) != len(new_columns):
    raise ValueError(
        f"Column count mismatch: DataFrame has {len(df.columns)} columns, "
        f"but new column list has {len(new_columns)} names."
    )

df.columns = new_columns

print("\nMeaningful column names rebuilt.")
print(f"Column count: {len(df.columns)}")

# Remove non-data rows
df = df.drop([0, 1])
df = df.reset_index(drop=True)

# Remove footer note row
df = df.iloc[:-1]
df = df.reset_index(drop=True)

print("\nNon-data header rows and footer note row removed")
print(f"Shape after removing non-data rows: {df.shape}")

# Check missing values after structural cleanup
print("\nMissing values after column selection:")
print(df.isna().sum())

# Convert numeric sector columns
for col in df.columns[4:]:
    df[col] = df[col].astype(str).str.replace(",", "", regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert time columns
for col in df.columns[:2]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nData types after numeric conversion:")
print(df.dtypes)

# Check for duplicates
print("\nShape before removing duplicates:")
print(df.shape)

duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows:")
print(duplicate_count)

df = df.drop_duplicates()
df = df.reset_index(drop=True)

print("\nShape after removing duplicates:")
print(df.shape)

# Final quality checks
print("\nFinal missing values:")
print(df.isna().sum())

print("\nPreview of cleaned data:")
print(df.head().to_string())

print("\nLast rows of cleaned data:")
print(df.tail().to_string())

# Save cleaned data
df.to_csv(CLEANED_FILE, index=False)

print(f'\nCleaned data saved to {CLEANED_FILE}')