import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regex pattern to match the time formats
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"

    # Search for the pattern in the input string
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Set default minutes to '00' if not provided
    start_minute = start_minute if start_minute else '00'
    end_minute = end_minute if end_minute else '00'

    # Validate hours and minutes
    if not (0 <= int(start_hour) <= 12 and 0 <= int(start_minute) < 60):
        raise ValueError("Invalid start time")
    if not (0 <= int(end_hour) <= 12 and 0 <= int(end_minute) < 60):
        raise ValueError("Invalid end time")

    # Convert start time to 24-hour format
    start_hour = int(start_hour)
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert end time to 24-hour format
    end_hour = int(end_hour)
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    # Format the times to 24-hour format
    start_time = f"{start_hour:02}:{start_minute}"
    end_time = f"{end_hour:02}:{end_minute}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()





