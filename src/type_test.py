from pathlib import Path
import csv

current_dir = Path(__file__).parent
project_root = current_dir.parent
csv_path = project_root / "data" / "raw" / "eia_sales_revenue_monthly_states.csv"

with open(csv_path, mode='r', encoding="utf-8-sig") as file:

    csv_reader = csv.reader(file)

    non_datarow1 = next(csv_reader)
    non_datarow2 = next(csv_reader)
    non_datarow3 = next(csv_reader)

    row = next(csv_reader)
   
    original_value = row[5]
    print(f'Original value: {original_value}')

    original_type = type(original_value)
    print(f'Original type: {original_type}')
    print(" ")

    # Remove commas
    no_commas = original_value.replace(",", "")

    converted_value = float(no_commas)
    print(f'Converted value: {converted_value}')

    converted_type = type(converted_value)
    print(f'Converted type: {converted_type}')
