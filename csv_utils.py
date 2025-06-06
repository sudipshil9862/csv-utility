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
        print(f"file not found: {file_path}")
    except Exception as e:
        print(f"error reading CSV: {e}")


def filter_rows(file_path, column_name, condition, value):
    result = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cell_value = row.get(column_name)
                if cell_value is None:
                    continue

                if condition == "contains":
                    if value.lower() in cell_value.lower():
                        result.append(row)
                else:
                    try:
                        cell_value_num = float(cell_value)
                        value_num = float(value)
                        if eval(f"{cell_value_num} {condition} {value_num}"):
                            result.append(row)
                    except ValueError:
                        continue
        return result
    except Exception as e:
        print(f"error filtering CSV: {e}")
        return []


def sort_rows(file_path, column_name, descending=False):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        try:
            sorted_rows = sorted(
                rows,
                key=lambda x: float(x[column_name]) if x[column_name] else float('-inf'),
                reverse=descending
            )
        except ValueError:
            sorted_rows = sorted(
                rows,
                key=lambda x: x[column_name].lower() if x[column_name] else "",
                reverse=descending
            )

        return sorted_rows
    except Exception as e:
        print(f"error sorting CSV: {e}")
        return []
