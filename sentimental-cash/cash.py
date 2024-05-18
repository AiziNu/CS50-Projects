def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
             return value
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")
            continue

def calculate_coins():
    change = get_float("Enter the amount of change owed: ")

    cents = round(change * 100)
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    num_coins = 0
    num_coins += cents // quarters
    cents %= quarters
    num_coins += cents // dimes
    cents %= dimes
    num_coins += cents // nickels
    cents %= nickels
    num_coins += cents // pennies

    print(num_coins)
calculate_coins()

