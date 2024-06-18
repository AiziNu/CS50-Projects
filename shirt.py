import sys


def main():
    #call our check arg funct that out agt needs to pass all conditions
    input_filename, output_filename = check_command_line_args()
    






def check_command_line_args():
    # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

  # Check if the input file has a .csv extension
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    if not input_filename.endswith(".csv"):
        sys.exit("Input file is not a CSV file")
    if not output_filename.endswith(".csv"):
        sys.exit("Output file is not a CSV file")

    return input_filename, output_filename


