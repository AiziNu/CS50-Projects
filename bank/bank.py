# create var greeting with user prompt
greeting = input("Please enter your greet. ").strip().split(" ")

#create conditions
if greeting[0].lower() == "hello":
    print("$0")
elif greeting[0].lower() == "h":
    print("$20")
