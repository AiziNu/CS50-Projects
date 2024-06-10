import emoji


user_input = input()
result = emoji.emojize(user_input, use_aliases=True)
print(result)

