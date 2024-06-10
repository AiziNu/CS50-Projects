from pyfiglet import Figlet
import sys

figlet = Figlet()
if len(sys.argv) < 2:
    sys.exit("Enter at leat two argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


