from pyfiglet import Figlet,FigletFont
import sys
import random


def main():
    # Parse command-line arguments
    args = sys.argv[1:]

    if len(args) not in [0, 2]:
        sys.exit("Usage: figlet.py [-f | --font FONT]")

    font = None
    if len(args) == 2:
        if args[0] not in ['-f', '--font']:
            sys.exit("First argument must be -f or --font")
        font = args[1]
        if font not in FigletFont.getFonts():
            sys.exit(f"Font '{font}' is not available. Use pyfiglet --list_fonts to see available fonts.")

    # Prompt user for text input
    user_input = input("Input: ")

    # Initialize Figlet with the specified or random font
    if font:
        figlet = Figlet(font=font)
    else:
        figlet = Figlet(font=random.choice(FigletFont.getFonts()))

    # Output the text in the desired font
    result = figlet.renderText(user_input)
    print(result)

main()
