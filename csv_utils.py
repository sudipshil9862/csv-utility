import csv

def read_and_display_csv(file_path, num_rows):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            all_rows = list(reader)
            total_rows = len(all_rows)

            print(f"\nTotal rows available (excluding header): {total_rows}")

            if num_rows > 30 and total_rows > 30:
                print("Cannot display more than 30 rows from this file. It contains more than 30 rows.")
                return

            if num_rows > total_rows:
                print(f"Only {total_rows} rows are available in the file. Showing all available rows...\n")
                num_rows = total_rows

            print(f"\n--- Displaying first {num_rows} row(s) ---\n")
            for i in range(num_rows):
                print(all_rows[i])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading CSV: {e}")

def filter_rows(rows, column_name, condition, value):
    result = []
    for row in rows:
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


def sort_rows(rows, column_name, descending=False):
    try:
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
        print(f"Error sorting rows: {e}")
        return []



def aggregate_column(file_path, column_name, operation):
    #performing aggregation on a numeric column - supported operation: sum, avg, min, max
    values = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    val = float(row[column_name])
                    values.append(val)
                except (ValueError, KeyError):
                    continue

        if not values:
            return f"No valid numeric values found in column '{column_name}'"

        operation = operation.lower()
        if operation == "sum":
            return sum(values)
        elif operation == "avg":
            return sum(values) / len(values)
        elif operation == "min":
            return min(values)
        elif operation == "max":
            return max(values)
        else:
            return f"unsupported operation: {operation}"

    except Exception as e:
        return f"error aggregating data: {e}"


def is_special_palindrome(value):
    #checking if the value is a palindrome and uses only A, D, V, B, N
    valid_chars = set("ADVBN")
    value = value.upper()

    if not value.isalpha():
        return False
    if value != value[::-1]:
        return False
    return all(char in valid_chars for char in value)

def count_special_palindromes(file_path):
    #returning a list of such palindromes and their count
    count = 0
    matches = set()

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for value in row.values():
                    if isinstance(value, str) and is_special_palindrome(value.strip()):
                        matches.add(value.strip().upper())
                        count += 1
        return matches, count
    except Exception as e:
        print(f"error counting palindromes: {e}")
        return set(), 0


def write_to_csv(output_path, rows, headers=None):
    if not rows:
        print("No data to write.")
        return

    if headers is None:
        headers = rows[0].keys()

    try:
        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Data written to {output_path}")
    except Exception as e:
        print(f"Failed to write file: {e}")
