import sys


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




#Function to check the command line arg
def check_commang_line_agr():
    #check how many elements in the command line
    if sys.argv < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 2:
        sys.exit("Too many command-line arguments")
    #check if its a Py file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
