def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #we will loop through s
    for char in s:
        if 2 <=len(s)<=6 and s[char].endswith(int) and s[char].startswith(str):
            return True
        else: False
        


main()
