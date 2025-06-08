import sys
import os
import unittest
import subprocess
from csv import DictReader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from csv_utils import (
    filter_rows,
    sort_rows,
    aggregate_column,
    count_special_palindromes
)

class TestCSVUtility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_csv_path = "data/fruits_sales_data.csv"
        cls.empty_csv_path = "data/empty.csv"

        with open(cls.test_csv_path, newline='', encoding='utf-8') as f:
            reader = DictReader(f)
            cls.rows = list(reader)

    def test_filter_numeric_greater_than(self):
        result = filter_rows(self.rows, "Quantity", ">", "8")
        self.assertEqual(len(result), 4)

    def test_filter_string_contains(self):
        result = filter_rows(self.rows, "Product", "contains", "Apple")
        self.assertEqual(len(result), 2)

    def test_sort_by_price_ascending(self):
        result = sort_rows(self.rows, "Price")
        prices = [float(row["Price"]) for row in result]
        self.assertEqual(prices, sorted(prices))

    def test_sort_by_quantity_descending(self):
        result = sort_rows(self.rows, "Quantity", descending=True)
        quantities = [int(row["Quantity"]) for row in result]
        self.assertEqual(quantities, sorted(quantities, reverse=True))

    def test_aggregate_sum_quantity(self):
        result = aggregate_column(self.test_csv_path, "Quantity", "sum")
        self.assertEqual(result, 59.0)

    def test_aggregate_max_price(self):
        result = aggregate_column(self.test_csv_path, "Price", "max")
        self.assertEqual(result, 1.5)

    def test_palindromes(self):
        palindromes, total = count_special_palindromes(self.test_csv_path)
        self.assertIn("BANAB", palindromes)
        self.assertEqual(total, 1)

    def test_empty_csv(self):
        with open(self.empty_csv_path, newline='', encoding='utf-8') as f:
            reader = DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 0)

    def test_invalid_column_for_filter(self):
	    result = subprocess.run(
		["python3", "main.py", "data/fruits_sales_data.csv", "-f", "Quantitys", ">", "5"],
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True
	    )
	    self.assertIn("Invalid column for filtering: 'Quantitys'", result.stdout)
	    self.assertIn("Available columns: Date, Product, Quantity, Price", result.stdout)
	    self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
