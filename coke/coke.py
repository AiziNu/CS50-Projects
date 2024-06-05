def main():
    amount_due = 50  # tottal amount of one bottle of coce
    accepted_coins = [5,10,25]  #accepted denomanation

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin
            print(f"Amount Due: {amount_due}")
        else:
            print("Invalid coin insert 5, 10 or 25 cents")

    change_owed = -amount_due  # calculate change owed
    print(f"Change Owed: {change_owed} cents")

main()





