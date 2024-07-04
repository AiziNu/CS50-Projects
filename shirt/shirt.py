import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check for valid file extensions and matching input/output extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid file extension. Only .jpg, .jpeg, and .png are allowed.")

    if input_ext != output_ext:
        sys.exit("Input and output file extensions do not match.")

    # Try to open the input image
    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit(f"Input file '{input_path}' not found.")

    # Open the shirt image
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("The overlay image 'shirt.png' was not found.")

    # Resize and crop the input image to match the size of the shirt image
    shirt_size = shirt.size
    input_image = ImageOps.fit(input_image, shirt_size, method=Image.BICUBIC)

    # Overlay the shirt onto the input image
    input_image.paste(shirt, shirt, shirt)

    # Save the resulting image to the output path
    try:
        input_image.save(output_path)
    except Exception as e:
        sys.exit(f"Error saving the output image: {e}")

if __name__ == "__main__":
    main()


