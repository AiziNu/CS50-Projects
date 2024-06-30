from datetime import date
import sys


def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except ValueError():
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))



def minutes_lived(year,month, day):
    dt = date(int(year), int(month), int(day))
    


if __name__ == "__main__":
    main()

