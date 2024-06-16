def main():
    while True:
        try:
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
                print(f"{round(percentage)}%")
            break


        except (ValueError, ZeroDivisionError):
            # Prompt the user again if input is invalid
            pass

main()

def main():
    ...


def convert(fraction):



def gauge(percentage):
     if percentage <= 1:
        return "E"
     elif percentage >=99:
        return "F"
     else:
        print(f"{round(percentage)}%")
        break



if __name__ == "__main__":
    main()
