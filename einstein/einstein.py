# create formula func

def einstein(mass_input):
    c = 300000000
    mass = int(mass_input)
    formula = mass * c**2
    return formula

def main():
    user_input= input("Enter mass: ")
    result = einstein(user_input)
    print(result)


main()
