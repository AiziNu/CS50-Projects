import sys
import os

def main():
    # Check the command line arguments
    check_command_line_args()

    # Try to open the file and read lines
    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Count lines of code excluding comments and blank lines
    loc = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            loc += 1

    print(loc)

# Function to check the command line arguments
def check_command_line_args():
    # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if the file has a .py extension
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
