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

    valid_extensions = ('.jpg', '.jpeg', '.png')

    # Check if both files have valid extensions
    if not input_file.lower().endswith(valid_extensions) or not output_file.lower().endswith(valid_extensions):
        sys.exit("Input and output files must have a valid image extension (.jpg, .jpeg, .png)")

    # Check if both files have the same extension
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output files must have the same extension")

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.exit(f"Input file '{input_file}' does not exist")


