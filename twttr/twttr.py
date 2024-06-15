def main():
    try:
        user_input = input("Enter your tweet: ")
        result = convert_twttr(user_input)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def convert_twttr(str_input):
    vowels = "AEIOUaeiou"
    return ''.join(char for char in str_input if char not in vowels)

if __name__ == "__main__":
    main()
