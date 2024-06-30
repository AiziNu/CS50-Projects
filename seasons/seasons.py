from datetime import date
import sys


def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except ValueError():
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))



def minutes_lived(year,month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError():
        return "Invalid date"
    tday = date.today()
    differ= tday - dt
    print(differ)



if __name__ == "__main__":
    main()

