# CSV Utility Tool

This is a command-line utility built in Python that performs various operations on CSV files. It supports reading, filtering, sorting, aggregating, writing results to a new file, and finding special palindromes in CSV data.

## Features

- **Preview CSV**: Show the first N rows.
- **Filter Rows**: Filter data based on column values using numeric or user-provided conditions or substring matching.
- **Sort Rows**: Sort data by a given column in ascending or descending order.
- **Aggregate Columns**: Calculate sum, average, min, or max on numeric columns.
- **Palindrome Detection**: Find and count special palindromes using only the letters A, D, V, B, N.
- **Save Results**: Write all output after operation to a new CSV file, new csv file name will be decided by user.user-provided

## Usage

Run the utility using:

```
python3 main.py <csv_file_path> [options]
```
## Options

`-n`, `--preview`   : Show the first N rows (max 30)
`-f`, `--filter`    : Filter rows. Usage: `-f <column> <operator> <value>` (e.g., `-f Quantity > 10`)
`-s`, `--sort`      : Sort rows by a column
`--desc`            : Sort in descending order
`-a`, `--aggregate` : Aggregate column. Usage: `-a <column> <operation>` (e.g., `-a Quantity sum`)
`--palindrome`      : Count special palindromes with only A, D, V, B, N
`-o`, `--output`    : Save the final result to a new CSV file

## Example Commands
Show top 5 rows:
```
./csv-utility data/fruits_sales_data.csv -n 5
```

Filter and sort:
```
./csv-utility data/fruits_sales_data.csv -f Quantity ">" 5 -s Price --desc
```

Aggregate and save to a new file:
```
./csv-utility data/fruits_sales_data.csv -a Quantity sum -o result/output.csv
```

Check for palindromes:
```
./csv-utility data/fruits_sales_data.csv --palindrome
```
multiple argparse simultaneously is possible:
```
./csv-utility data/fruits_sales_data.csv   -n 5   -f Quantity ">" 5   -s Pricew --desc   -a Quantity sum   --palindrome   -o result/full_output.csv
```

## Running Test cases
Unit tests are located under the tests/ directory. Run them using:
```
python3 tests/test_csv_utility.py
```
Tests cover:
Filtering by value and substring, sorting numeric and string columns, aggregation (sum, max), palindrome detection, handling empty files, invalid column errors

### Sample Data
sample csv files are provided under the `data/` folder for example and test cases purposes:
`fruits_sales_data.csv`, `empty.csv`


## NOTE:
1. this tool can handle empty csv as input
2. it can handle incorrect column name
3. giving multiple options simultaneously - can be done easily 
