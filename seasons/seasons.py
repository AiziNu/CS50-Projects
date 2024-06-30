from datetime import date, datetime
import inflect
import sys

def main():
    dob_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")

    today = date.today()
    age_in_minutes = calculate_age_in_minutes(birth_date, today)
    print(minutes_to_words(age_in_minutes))

def calculate_age_in_minutes(birth_date, today):
    delta = today - birth_date
    return delta.days * 24 * 60

def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").replace(",", "").replace("-", " ")

if __name__ == "__main__":
    main()


