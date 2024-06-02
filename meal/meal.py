def main():
    time = input("What time is it? ").strip()

    hours = convert(time)


    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    hour, minute = time.split(":")

    #converting hour and min to inegers
    hour = int(hour)
    minute = int(minute)

    # Convert the time to a float representing hours
    return hour + minute / 60.0



main()
if __name__ == "__main__":
    main()
