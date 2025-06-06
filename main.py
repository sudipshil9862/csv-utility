from csv_utils import read_and_display_csv, filter_rows, sort_rows

if __name__ == "__main__":
    file_path = "data/fruits_sales_data.csv"

    print("\n🔹 Showing first 3 rows:")
    read_and_display_csv(file_path)

    print("\n🔹 Filter: Quantity > 10")
    filtered = filter_rows(file_path, "Quantity", ">", "10")
    for row in filtered:
        print(row)

    print("\n🔹 Filter: Product contains 'Apple'")
    filtered = filter_rows(file_path, "Product", "contains", "Apple")
    for row in filtered:
        print(row)

    print("\n🔹 Sort by Price (ascending):")
    sorted_data = sort_rows(file_path, "Price")
    for row in sorted_data[:3]:  # Display only top 3
        print(row)

    print("\n🔹 Sort by Quantity (descending):")
    sorted_data = sort_rows(file_path, "Quantity", descending=True)
    for row in sorted_data[:3]:
        print(row)
