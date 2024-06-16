def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # we check all condition one by one
    #1.length of s it has ti be between 2 to 6 inclusiev
    if len(s)< 2 or len(s) > 6:
        return False

    #2. chech if plates starts with 2 letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    #3.Check extra space or puctuations
    if not s.isalnum():
        return False

     # Check if all characters after the first two are digits
    for char in s[2:]:
        if not char.isdigit():
            return False

    # Rule 5: The first number used cannot be '0'
    if len(s) > 2 and s[2] == "0":
        return False

    return True



if __name__ == "__main__":
    main()
