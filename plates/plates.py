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
    of 




main()
