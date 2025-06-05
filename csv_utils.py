import csv

def read_and_display_csv(file_path, num_rows=3):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f"\n--- Showing first {num_rows} rows from: {file_path} ---\n")
            for i, row in enumerate(reader):
                if i >= num_rows:
                    break
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading CSV: {e}")
