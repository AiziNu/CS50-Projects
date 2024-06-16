

def main():
    pass


def convert(fraction):
    try:
        #get prompt from user
        fraction = input("Fraction: ")

        x,y = fraction.split('/')

        x = int(x)
        y = int(y)

            #validate canditions
        if x > y or y == "0":
            raise ValueError

        return round((x / y) * 100)


    except ValueError:
        raise ValueError("Invalid input")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")



def gauge(percentage):
     if percentage <= 1:
        return "E"
     elif percentage >=99:
        return "F"
     else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()
