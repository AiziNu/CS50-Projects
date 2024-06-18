import sys
import csv
def main():
    #call check agument funct that it has to pass all condition
    input_file, output_file = check_command_line_args()

    #we use try and catch if there anyy eroor will occur
    try:
        with open(input_file, mode = 'r') as infile:
            reader = csv.DictReader(infile)

            #prepare the file for output CSV file
            students = []
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                students.append({"first": first, "last": last, "house": house })

        #write the processed data to outout
        with open(output_file, mode='w') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


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

if __name__ == "__main__":
    main()
