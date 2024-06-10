import emoji


user_input = input("Input: ")
result = emoji.emojize("Output: ", user_input, use_aliases=True)
print(result)

