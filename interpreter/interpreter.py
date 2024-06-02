
def main():
      # Prompt the user for an arithmetic expression
    expression = input('Expression (x, y, z): ').strip()

    # Split the expression into components
    x, y, z = expression.split(" ")

    # Convert x and z to integers
    x = int(x)
    z = int(y)

    # Perform the appropriate arithmetic operation
    if y == "+":
        result =  x + z
    elif y == "-":
        result =  x - z
    elif y == "*":
        result =  x * z
    elif y == "/":
        result =  x / z
    else:
        print("Invalid operator")
        return

    print(f"{result:1f}")


main()


