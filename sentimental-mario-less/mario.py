
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 8:
             return value
        except ValueError:
            continue

def draw_piramid():
    height = get_int("Enter the height of the pyramid: ")

    for i in range(1, height + 1):
        print(" " * (height-1) + "#" * i, end="")
        print()

draw_piramid()
