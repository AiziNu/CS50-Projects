def main():
    user_input = input("Enter your tweet: ")
    result = convert_twttr(user_input)
    print(result)



def convert_twttr(str_input):
    new_string = ""
    vowels = ["a","e", "i", "o", "u"]

    for char in str_input:
        if char.lower() in vowels:
            continue
        else:
            new_string += char

    return new_string

main()
