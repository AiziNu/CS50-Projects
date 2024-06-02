## get input from user
user_thought = input("Enter the aswer: ")

# create conditions
if user_thought == '42' or user_thought == ('forty two').capitalize() or user_thought == 'forty-two':
    print("Yes")
else:
    print("No")
