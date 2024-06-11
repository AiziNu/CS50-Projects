import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in ['1', '2', '3']:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Enter valid integer")


def generate_integer(level):
    ...
