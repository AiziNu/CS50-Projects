#create main func for get user prompt

def main():
    user_input = input("Enter camelCase: ")
    snake_case = convert_snakeCase(user_input)


# create funct with converts to snake_case
def convert_snakeCase(s):
    new_string = ""
    for i in s:
        if (i.isupper()):
            new_string += "*"+1
        else:
            new_string +=i
