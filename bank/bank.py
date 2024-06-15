def main():
    greeting = input("Please enter your greet. ").strip().lower()
    print()



def value(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")



if __name__ == "__main__":
    main()
