def main():
    owner = input("Enter the account owner's name: ")
    balance = 0.0
    while True:
        print("\n1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            balance = add_funds(balance, amount)
            print(f"${amount} deposited successfully for {owner}.")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            balance, message = withdraw_funds(balance, amount)
            print(message)
        elif choice == '3':
            print(check_balance(owner, balance))
        elif choice == '4':
            print("Thank you for using the deposit calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_funds(balance, amount):
    return balance + amount

def withdraw_funds(balance, amount):
    if amount <= balance:
        return balance - amount, f"${amount} withdrawn successfully."
    else:
        return balance, "Insufficient funds."

def check_balance(owner, balance):
    return f"{owner}'s current balance: ${balance}"

if __name__ == "__main__":
    main()
