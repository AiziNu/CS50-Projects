# create var greeting with user prompt
greeting = input("Please enter your greet. ").strip().lower()

#create conditions
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
