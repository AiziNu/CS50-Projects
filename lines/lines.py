import sys


def main():
    #check the command line
    check_commang_line_agr()

    # try to open the file

    # if cant this means file isnot exist

    #Loop through the lines and check if starts with # or whitespace




#Function to check the command line arg
def check_commang_line_agr():
    #check how many elements in the command line
    if sys.argv < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 2:
        sys.exit("Too many command-line arguments")
    #check if its a Py file
    if ".py" not in sys.argv[1]

if __name__ == "__main__":
    main()
