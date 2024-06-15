def main():
    user_input = input("Enter your tweet: ")
    result = convert_twttr(user_input)
    print(result)



def convert_twttr(str_input):
    new_string = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for char in str_input:
        if char in vowels:
            continue
        else:
            new_string += char

    return new_string

if __name__ == "__main__":
    main()
