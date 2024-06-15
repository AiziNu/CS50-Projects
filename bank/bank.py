# create var greeting with user prompt
greeting = input("Please enter your greet. ").strip().lower()

#create conditions
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")



def main():
    ...


def value(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")



if __name__ == "__main__":
    main()
