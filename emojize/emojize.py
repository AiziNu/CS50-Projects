import emoji


user_input = input("Input: ")
result = emoji.emojize(f"Output: {user_input} " , language='alias')
print(result)

