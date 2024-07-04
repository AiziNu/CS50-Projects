import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Validate file extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output files must be .jpg, .jpeg, or .png")

    if input_ext != output_ext:
        sys.exit("Input and output files must have the same extension")

    # Check if input file exists
    if not os.path.exists(input_path):
        sys.exit(f"Input file '{input_path}' does not exist")

    try:
        # Open the input image and the shirt image
        input_image = Image.open(input_path)
        shirt = Image.open("shirt.png")

        # Resize and crop the input image to the size of the shirt image
        size = shirt.size
        input_image = ImageOps.fit(input_image, size)

        # Overlay the shirt on the input image
        input_image.paste(shirt, shirt)

        # Save the result
        input_image.save(output_path)
        print(f"Output saved to '{output_path}'")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



