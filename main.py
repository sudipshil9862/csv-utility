import argparse
import os
from csv_utils import (
    read_and_display_csv, filter_rows, sort_rows,
    aggregate_column, count_special_palindromes, write_to_csv
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV File Utility Tool")

    parser.add_argument("file", help="Path to the input CSV file")

    #CLI flags
    parser.add_argument("-n", "--preview", type=int, help="Show N rows (max 30)")
    parser.add_argument("-f", "--filter", nargs=3, metavar=('column', 'operator', 'value'),
                        help="Filter rows. Example: -f Quantity > 10")
    parser.add_argument("-s", "--sort", metavar="column", help="Sort rows by column")
    parser.add_argument("--desc", action="store_true", help="Sort descending")
    parser.add_argument("-a", "--aggregate", nargs=2, metavar=("column", "operation"),
                        help="Aggregate column with operation: sum, avg, min, max")
    parser.add_argument("--palindrome", action="store_true", help="Count special palindromes")
    parser.add_argument("-o", "--output", help="Write result to a new CSV file")

    args = parser.parse_args()

    file_path = args.file
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)

    if args.preview is not None:
        read_and_display_csv(file_path, args.preview)

    from csv import DictReader
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = DictReader(f)
        rows = list(reader)
        if not rows and not (args.aggregate or args.palindrome):
            print(f"The file '{file_path}' contains no data rows to display.")
            exit(0)

    headers = rows[0].keys() if rows else []

    if args.filter:
        col, op, val = args.filter
        rows = filter_rows(rows, col, op, val)
        if col not in headers:
            print(f"\nInvalid column for filtering: '{col}' \nAvailable columns: {', '.join(headers)}")
            exit(1)

    if args.sort:
        if args.sort not in headers:
            print(f"\nInvalid column for sorting: '{args.sort}' \nAvailable columns: {', '.join(headers)}")
            exit(1)
        rows = sort_rows(rows, args.sort, descending=args.desc)

    if args.aggregate:
        col, op = args.aggregate
        if col not in headers:
            print(f"\nInvalid column for aggregation: '{col}' \nAvailable columns: {', '.join(headers)}")
            exit(1)
        result = aggregate_column(file_path, col, op)
        print(f"\nAggregation result for '{col}' ({op}): {result}")

    if args.palindrome:
        palindromes, total = count_special_palindromes(file_path)
        print(f"\nFound {total} special palindrome(s): {sorted(palindromes)}")

    if args.output:
        write_to_csv(args.output, rows)
    elif args.filter or args.sort:
        print("\nFinal result:")
        for row in rows:
            print(row)
    elif not (args.preview or args.aggregate or args.palindrome):
        print("\nFinal result:")
        for row in rows:
            print(row)
