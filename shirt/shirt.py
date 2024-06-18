import sys
import os
from PIL import Image, ImageOps

def check_command_line_args():
     # Check the number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Supported image extensions
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


def main():
    # Check command-line arguments and get filenames
    input_file, output_file = check_command_line_args()

    try:
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")

        # Open the input image
        input_image = Image.open(input_file)
        print(f"Opened input image: {input_image}")

        # Open the shirt image
        shirt_image = Image.open("shirt.png")
        print(f"Opened shirt image: {shirt_image}")

        # Resize and crop the input image to match the size of the shirt image
        fitted_image = ImageOps.fit(input_image, shirt_image.size, method=Image.LANCZOS, bleed=0.0, centering=(0.5, 0.5))
        print(f"Fitted image size: {fitted_image.size}")

        # Overlay the shirt image on the fitted input image using transparency mask
        fitted_image.paste(shirt_image, (0, 0), shirt_image)
        print("Pasted shirt image onto fitted image")

        # Save the resulting image to the output file
        fitted_image.save(output_file)
        print(f"Saved output image: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


