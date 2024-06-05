def main():
    while True:

        #get prompt from user
        fraction = input("Fraction: ")

        x,y = fraction.split('/')

        x = int(x)
        y = int(y)

        #validate canditions
        if x > y or y == "0":
            raise ValueError

        percentage = (x/y)*100

        if percentage <= 1:
            print("E")
        elif percentage >=99:
            print("F")
        else:
            print(f"round")


