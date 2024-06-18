def main():
    #call check agument funct that it has to pass all condition
    







def check_command_line_args():
    # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

  # Check if the file has a .csv extension
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    return filename
