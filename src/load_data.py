# Import Path from pathlib so we can build file paths in a clean way.
# This helps us avoid hardcoding the full Mac file path.
from pathlib import Path 

# Import Python's built-in CSV module so we can read CSV files properly.
import csv 


# __file__ represents the current Python file: load_data.py
# Path(__file__).parent gets the folder that load_data.py is inside.
# Since load_data.py is inside src/, current_dir becomes the src folder.
current_dir = Path(__file__).parent


# current_dir.parent goes up one folder level.
# Since current_dir is src/, project_root becomes the main project folder:
# smart-utilities-analytics/
project_root = current_dir.parent


# Build the path to the raw CSV file.
# The / operator joins folder names together when using Path.
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
    # This lets Python read the file row by row.
    # Each row will be read as a list of values.
    csv_reader = csv.reader(file)


    # Read the first row of the CSV manually.
    # next(csv_reader) grabs the next available row.
    # Since this is the first call to next(), it grabs the first row.
    # In this dataset, the first row contains sector labels like RESIDENTIAL and COMMERCIAL.
    header = next(csv_reader)


    # Print the first row so we can inspect the raw structure of the CSV.
    print("HEADER:", header)


    # Print a divider line to make the output easier to read.
    # "-" * 50 means repeat "-" fifty times.
    print("-" * 50)


    # Loop through the remaining rows in the CSV.
    # enumerate gives us two things:
    # i = the row counter, starting at 0
    # row = the actual CSV row as a list
    for i, row in enumerate(csv_reader):

        # Only print the first 5 rows after the header.
        # Since i starts at 0, i < 5 allows i = 0, 1, 2, 3, 4.
        if i < 5:

            # Print the row number and the row contents.
            # i + 1 makes the displayed row number start at 1 instead of 0.
            print(f'Row {i+1}: {row}')

        # Once we have printed 5 rows, stop the loop.
        # This prevents the terminal from printing all 9,000+ rows.
        else:
            break

