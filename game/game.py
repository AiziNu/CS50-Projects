import random


def main():
    # get user promt n until what number they want to guess
    print("Enter number of Level from 1 to 100 ")
    n = int(input("Level: "))
    rand_guess = random.randrange(1, n+1)

    guess = int(input("Guess: "))

    while True:
        if guess < rand_guess:
            print("Too small")
        elif guess > rand_guess


