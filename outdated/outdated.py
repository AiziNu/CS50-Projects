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
        user_input = input("Enter a date (month-day-year or month day, year): ")
        date_parts = user_input.split()
        if len(date_parts) == 3:
            month_name, day, year = date_parts
            month_number = get_month_number(month_name)
            if month_number:
                formatted_date = f"{year}-{month_number:02d}-{int(day):02d}"
                print(f"Formatted date: {formatted_date}")
                break
        elif len(date_parts) == 1:
            if validate_date(date_parts[0]):
                formatted_date = date_parts[0].replace("/", "-")
                print(f"Formatted date: {formatted_date}")
                break
        print("Invalid date format. Please try again.")

main()
