import sys
import csv
from tabulate import tabulate

# Check if exactly one command-line argument is given
if len(sys.argv) != 2:
    print("Too few command-line arguments")
    sys.exit()

filename = sys.argv[1]

# Check if the file name ends with .csv
if not filename.endswith('.csv'):
    print("Not a CSV file")
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


def main():
    #call if aour iptut pass all parameter
    check_command_line_args()

    try:
        

def check_command_line_args():
    # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if the file has a .py extension
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
