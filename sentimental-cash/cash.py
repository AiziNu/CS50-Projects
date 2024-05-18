def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0
             return value
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")
            continue

def draw_piramid():
    height = get_int("Enter the height of the pyramid: ")

    for i in range(1, height + 1):
        print(" " * (height -i) + "#" * i, end="")
        print()

draw_piramid()
