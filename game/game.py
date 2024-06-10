import random


def main():
    # get user promt n until what number they want to guess
    print("Enter number of Level from 1 to 100 ")

    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <=100:
                break
            else:
                print("Please enter number between 1 to 100")
        except ValueError:
            print("Enter valid integer")
    #generate random integer
    rand_guess = random.randint(1, n+1)


    #loop continiusly until user get correct number
    while True:

         try:
            guess = int(input("Guess: "))
                #check guess and print too low or too high
            if guess < rand_guess:
                print("Too small")
            elif guess > rand_guess:
                print("Too large")
            else:
                print("Just right")
                break
         except ValueError:
             print("Enter valid integer")

main()




