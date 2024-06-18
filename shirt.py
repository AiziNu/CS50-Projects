import sys
import os
from PIL import Image, ImageOps


def main():
    #call our check arg funct that out agt needs to pass all conditions
    input_file, output_file = check_command_line_args()

    try:
        # Open the input image
        input_image = Image.open(input_file)

        # Open the shirt image
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the size of the shirt image
        fitted_image = ImageOps.fit(input_image, shirt_image.size, method=Image.LANCZOS, bleed=0.0, centering=(0.5, 0.5))

        # Overlay the shirt image on the fitted input image
        fitted_image.paste(shirt_image, (0, 0), shirt_image)

        # Save the resulting image to the output file
        fitted_image.save(output_file)

    except Exception as e:
        sys.exit(f"An error occurred: {e}")



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

    return input_file, output_file


if __name__ == "__main__":
    main()
