

def get_int(n):
    while True:
        try:
            value = int(input(n))
            if 1 <= value <= 8:
            return value
        except ValueError:
            continue

def draw_piramid():
    height = get_int("Enter the height of the pyramid: ")

    for i in range(1, height+1):
        print(" " * (height-1) + "#" * i)

draw_piramid()
