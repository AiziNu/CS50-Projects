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

        percentage = 


