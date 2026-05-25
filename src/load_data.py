# Import Path from pathlib so we can build file paths in a clean way.
# This helps us avoid hardcoding the full Mac file path.
from pathlib import Path 

# Import Python's built-in CSV module so we can read CSV files properly.
import csv 

# Path(__file__).parent gets the folder that load_data.py is inside.
# Since load_data.py is inside src/, current_dir becomes the src folder.
current_dir = Path(__file__).parent

# Since current_dir is src/, project_root becomes the main project folder:
# smart-utilities-analytics/
project_root = current_dir.parent


# Build the path to the raw CSV file.
# This creates:
# smart-utilities-analytics/data/raw/eia_sales_revenue_monthly_states.csv
csv_path = project_root / "data" / "raw" / "eia_sales_revenue_monthly_states.csv"


# Open the CSV file in read mode.
# mode='r' means we are reading the file, not writing to it.
# encoding="utf-8-sig" tells Python to read the file as UTF-8
# and automatically remove the Excel byte-order mark if it exists.
# The with statement automatically closes the file when we are done.
with open(csv_path, mode='r', encoding="utf-8-sig") as file:

    # Create a CSV reader object.
    csv_reader = csv.reader(file)

    # Read the first row of the CSV manually.
    # next(csv_reader) grabs the next available row.
    # In this dataset, the first row contains sector labels like RESIDENTIAL and COMMERCIAL.
    header = next(csv_reader)


    # Print the first row so we can inspect the raw structure of the CSV.
    print("HEADER:", header)
    print("-" * 50)

    # Loop through the remaining rows in the CSV.
    for i, row in enumerate(csv_reader):
        if i < 5:
            print(f'Row {i+1}: {row}')
        else:
            break

