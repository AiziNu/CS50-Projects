def get_month_number(month_name):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return months.get(month_name, None)

def validate_date(date_str):
    try:
        parts = date_str.split("/")
        if len(parts) != 3:
            return False
        month, day, year = map(int, parts)
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

def main():
    while True:
        user_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ")

        # Handling "Month DD, YYYY" format
        if "," in user_input:
            try:
                month_name, day_year = user_input.split(" ", 1)
                day, year = day_year.split(", ")
                day = int(day)
                year = int(year)
                month_number = get_month_number(month_name)
                if month_number and 1 <= day <= 31:
                    formatted_date = f"{year:04d}-{month_number:02d}-{day:02d}"
                    print(formatted_date)
                    break
            except (ValueError, IndexError):
                pass

        # Handling "MM/DD/YYYY" format
        elif validate_date(user_input):
            month, day, year = map(int, user_input.split("/"))
            formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
            print(formatted_date)
            break

        print("Invalid date format. Please try again.")
main()
