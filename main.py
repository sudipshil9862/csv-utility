from csv_utils import read_and_display_csv, filter_rows, sort_rows, aggregate_column, count_special_palindromes
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV File Utility Tool")
    parser.add_argument("file", help="Path to the input CSV file")
    args = parser.parse_args()

    file_path = args.file
    if not os.path.exists(file_path):
        print(f"file not found: {file_path}")
        exit(1)

    try:
        num_to_show = int(input("Enter how many rows you want to see (max 30): "))
    except ValueError:
        print("invalid input. Must be an integer.")
        exit(1)
    read_and_display_csv(file_path, num_to_show)

    print("\n Filter: Quantity > 10")
    filtered = filter_rows(file_path, "Quantity", ">", "10")
    for row in filtered:
        print(row)

    print("\n Filter: Product contains 'Apple'")
    filtered = filter_rows(file_path, "Product", "contains", "Apple")
    for row in filtered:
        print(row)

    print("\n Sort by Price (ascending):")
    sorted_data = sort_rows(file_path, "Price")
    for row in sorted_data[:3]:  # Display only top 3
        print(row)

    print("\n Sort by Quantity (descending):")
    sorted_data = sort_rows(file_path, "Quantity", descending=True)
    for row in sorted_data[:3]:
        print(row)

    print("\n Aggregate: Sum of Quantity")
    print("Result:", aggregate_column(file_path, "Quantity", "sum"))

    print("\n Aggregate: Avarage of Price")
    print("Result:", aggregate_column(file_path, "Price", "avg"))

    print("\n Aggregate: minimum of Price")
    print("Result:", aggregate_column(file_path, "Price", "min"))

    print("\n Aggregate: maximum of  Quantity")
    print("Result:", aggregate_column(file_path, "Quantity", "max"))



    print("\ncounting special palindromes (A, D, V, B, N only)")
    palindromes, total = count_special_palindromes(file_path)
    print(f"found {total} palindrome(s): {sorted(palindromes)}")


