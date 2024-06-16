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

    #4Check s is finishing with num
    #Loop through s, if ther ius a num update found num to True
    found_num = False
    for char in s:
        if char.isdigit():
            found_num = True
        elif found_num and char.isalpha():
            return False

     # Rule 5: The first number used cannot be '0'
    # for char in s:
    #     if char.isdigit():
    #         if char == "0":
    #             return False
    #         break
    return True



if __name__ == "__main__":
    main()
