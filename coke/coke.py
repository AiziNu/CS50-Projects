def main():
    amount_due = 50  # tottal amount of one bottle of coce
    accepted_coins = [5,10,25]  #accepted denomanation

    while amount_due > 0:
        print(f"Amount Due: {amount_due} cents")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin
        else:
            print("Invalid coin. Please insert a coin of 25, 10, or 5 cents.")

    change_owed = -amount_due  # calculate change owed
    print(f"Change Owed: {change_owed} cents")

main()





