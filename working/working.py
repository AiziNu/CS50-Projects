import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression pattern to match the input format with proper spacing
    pattern = re.compile(r'^\s*(\d{1,2})(:(\d{2}))?\s*(AM|PM)\s*to\s*(\d{1,2})(:(\d{2}))?\s*(AM|PM)\s*$')
    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.group(1), match.group(3), match.group(4), match.group(5), match.group(7), match.group(8)

    # Ensure minutes are present if colons are present
    if (match.group(2) and not start_minute) or (match.group(6) and not end_minute):
        raise ValueError("Invalid format")

    # Default minutes to "00" if they are not provided
    if start_minute is None:
        start_minute = "00"
    if end_minute is None:
        end_minute = "00"

    # Validate and convert times
    start_time_24 = to_24_hour_format(start_hour, start_minute, start_period)
    end_time_24 = to_24_hour_format(end_hour, end_minute, end_period)

    return f"{start_time_24} to {end_time_24}"

def to_24_hour_format(hour, minute, period):
    hour = int(hour)
    minute = int(minute)

    if not (1 <= hour <= 12 or 0 <= minute < 60):
        raise ValueError("Invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()


