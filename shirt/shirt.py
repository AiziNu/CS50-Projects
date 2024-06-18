import sys
from PIL import Image, ImageOps

def main():
    # Check for command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    # Check file extensions
    input_ext = sys.argv[1].lower().split('.')[-1]
    output_ext = sys.argv[2].lower().split('.')[-1]
    if input_ext not in ['jpg', 'jpeg', 'png'] or output_ext not in ['jpg', 'jpeg', 'png']:
        sys.exit("Input and output files must be JPEG or PNG")

    if input_ext != output_ext:
        sys.exit("Input and output files must have the same extension")

    # Check if input file exists
    if not os.path.exists(sys.argv[1]):
        sys.exit("Input file does not exist")

    # Open input image
    input_image = Image.open(sys.argv[1])

    # Resize and crop input image
    size = (200, 200) # Replace with actual size of shirt.png
    resized_input = ImageOps.fit(input_image, size, Image.ANTIALIAS)

    # Open shirt image
    shirt_image = Image.open('shirt.png')

    # Overlay images
    resized_input.paste(shirt_image, (0, 0), shirt_image)

    # Save result
    resized_input.save(sys.argv[2])

if __name__ == "__main__":
    main()
