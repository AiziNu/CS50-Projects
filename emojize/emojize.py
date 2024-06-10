import emoji


user_input = input("Input: ")
result = emoji.emojize("Output: ", user_input, language='alias')
print(result)

