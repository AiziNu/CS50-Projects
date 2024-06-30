from datetime import date, datetime, timedelta
import inflect
import sys

def calculate_age_in_minutes(birth_date):
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = date.today()
        age = today - birth_date.date()
        age_in_minutes = int(age.total_seconds() / 60)
        return age_in_minutes
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

def format_minutes_in_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="")

def main():
    user_input = input("Enter your date of birth (YYYY-MM-DD): ")
    age_in_minutes = calculate_age_in_minutes(user_input)
    age_in_words = format_minutes_in_words(age_in_minutes)
    print(f"You are approximately {age_in_words} minutes old!")

if __name__ == "__main__":
    main()
