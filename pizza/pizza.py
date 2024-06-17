import sys
import csv
from tabulate import tabulate


def main(filename):
    #call if aour iptut pass all parameter
    check_command_line_args()

    try:
    # Read the CSV file into a list of lists
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

    # Use tabulate to print the table in grid format
        print(tabulate(data, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        print(f"File {filename} does not exist")
        sys.exit(1)



def check_command_line_args():
    # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

  # Check if the file has a .csv extension
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    return filename

if __name__ == "__main__":
    filename = check_command_line_args()
    main(filename)
