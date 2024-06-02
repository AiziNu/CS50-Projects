## get input from user
user_thought = input("Enter the aswer: ").strip()

# create conditions
if user_thought == '42' or user_thought.lower() == 'forty two' or user_thought.lower() == 'forty-two':
    print("Yes")
else:
    print("No")
