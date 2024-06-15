def main():
    user_input = input("Enter your tweet: ")
    result = convert_twttr(user_input)
    print(result)

def convert_twttr(str_input):
    vowels = "AEIOUaeiou"
    return ''.join(char for char in str_input if char not in vowels)

if __name__ == "__main__":
    main()
