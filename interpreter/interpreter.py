
def main():
      # Prompt the user for an arithmetic expression
    expression = input('Expression (x, y,z): ').strip()

    # Split the expression into components
    x, y, z = expression.split(" ")

    # Convert x and z to integers
    x = int(x)
    y = int(y)
    

