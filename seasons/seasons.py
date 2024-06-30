from datetime import date
import inflect
import sys

p = inflect.engine()

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
    minutes = int(differ.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="") + " minutes"
    print(msg)



if __name__ == "__main__":
    main()

