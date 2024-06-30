from datetime import date

def calculate_age_in_minutes(birth_date):
    today = date.today()
    age = today - birth_date
    age_in_minutes = age.days * 24 * 60
    return age_in_minutes

def main():
    try:
        user_input = input("Enter your date of birth (YYYY-MM-DD): ")
        year, month, day = map(int, user_input.split("-"))
        birth_date = date(year, month, day)
        age_in_minutes = calculate_age_in_minutes(birth_date)

        # Convert age to English words
        # You can use the 'inflect' library for this, as mentioned in the hints

        print(age_in_minutes)
    except ValueError:
        print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()


