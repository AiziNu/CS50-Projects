def main():
    user_input = input("What time is it? ").strip().split(":")
    print(user_input)
    if convert(user_input):
        

def convert(time):
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        return



if __name__ == "__main__":
    main()
