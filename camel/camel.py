#create main func for get user prompt

def main():
    user_input = input("Enter camelCase: ")
    snake_case = convert_snakeCase(user_input)
    print(snake_case)


# create funct with converts to snake_case
def convert_snakeCase(camel_case):
    new_string = ""
    for char in camel_case:
        if char.isupper():
            new_string +="_" + char.lower()
        else:
            new_string += char
    x = new_string.split("*")
    x.remove('')
    print(x)

main()
