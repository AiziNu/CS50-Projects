# create var greeting with user prompt
greeting = input("Please enter your greet. ").strip()

#create conditions
if greeting.lower() == "hello":
    print("$0")
elif greeting[0].lower() == "h":
    print("$20")
