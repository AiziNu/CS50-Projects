import sys
import csv
from tabulate import tabulate

# Check if exactly one command-line argument is given
if len(sys.argv) != 2:
    print("Usage: python pizza.py <filename>")
    sys.exit()

filename = sys.argv[1]

# Check if the file name ends with .csv
if not filename.endswith('.csv'):
    print("File must be a CSV file with a .csv extension")
    sys.exit()

try:
    # Read the CSV file into a list of lists
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Use tabulate to print the table in grid format
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    print(f"File {filename} does not exist")
    sys.exit()
