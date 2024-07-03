import datetime

def main():
    users = {}
    current_user = None

    while True:
        if current_user is None:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                register_user(users, username, password)
                print(f"User {username} registered successfully.")
            elif choice == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                current_user = login_user(users, username, password)
                if current_user:
                    print(f"Welcome, {username}!")
                else:
                    print("Invalid username or password. Please try again.")
            elif choice == '3':
                print("Thank you for using the deposit calculator.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"\nLogged in as {current_user['name']}")
            print("1. Deposit Funds")
            print("2. Withdraw Funds")
            print("3. Check Balance")
            print("4. Show Transaction History")
            print("5. Calculate Interest")
            print("6. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                add_funds(current_user, amount)
                print(f"${amount} deposited successfully.")
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                balance, message = withdraw_funds(current_user, amount)
                print(message)
            elif choice == '3':
                print(check_balance(current_user))
            elif choice == '4':
                show_transaction_history(current_user)
            elif choice == '5':
                rate = float(input("Enter annual interest rate (as a percentage): "))
                years = float(input("Enter the number of years: "))
                interest = calculate_interest(current_user, rate, years)
                print(f"Interest accrued over {years} years at {rate}%: ${interest:.2f}")
            elif choice == '6':
                current_user = None
                print("Logged out successfully.")
            else:
                print("Invalid choice. Please try again.")

def register_user(users, username, password):
    if username in users:
        raise ValueError("Username already exists")
    users[username] = {
        'name': username,
        'password': password,
        'balance': 0.0,
        'transactions': []
    }

def login_user(users, username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return user
    return None

def add_funds(user_data, amount):
    user_data['balance'] += amount
    user_data['transactions'].append((datetime.datetime.now(), 'Deposit', amount))

def withdraw_funds(user_data, amount):
    if amount <= user_data['balance']:
        user_data['balance'] -= amount
        user_data['transactions'].append((datetime.datetime.now(), 'Withdraw', amount))
        return user_data['balance'], f"${amount} withdrawn successfully."
    else:
        return user_data['balance'], "Insufficient funds."

def check_balance(user_data):
    return f"{user_data['name']}'s current balance: ${user_data['balance']}"

def show_transaction_history(user_data):
    if not user_data['transactions']:
        print("No transactions found.")
        return
    print("Transaction history:")
    for date, type, amount in user_data['transactions']:
        print(f"{date} - {type}: ${amount}")

def calculate_interest(user_data, rate, years):
    return user_data['balance'] * (rate / 100) * years

if __name__ == "__main__":
    main()
