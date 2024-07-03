# Deposit Calculator

## Description

The Deposit Calculator is a Python-based application that allows users to manage their financial transactions. Users can register an account, log in, deposit funds, withdraw funds, check their balance, view transaction history, and calculate interest on their balance over a specified period. This project serves as a final project for CS50, demonstrating the use of multiple functions, user interaction, and unit testing with pytest.

## Features

- **User Registration and Login**: Register new users and allow existing users to log in.
- **Deposit Funds**: Add money to the user's account.
- **Withdraw Funds**: Withdraw money from the user's account, with validation for sufficient balance.
- **Check Balance**: Display the current balance of the user's account.
- **Transaction History**: Show a history of all transactions made by the user.
- **Interest Calculation**: Calculate the interest on the user's balance over a specified period and interest rate.

## Project Structure


## Installation

1. **Clone the repository or download the project files.**
2. **Navigate to the project directory:**

    ```sh
    cd my_final_project
    ```

3. **Install any required dependencies using pip:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main program:**

    ```sh
    python project.py
    ```

    Follow the on-screen instructions to register a new account, log in, and perform various financial transactions.

## Running Tests

1. **Run the tests using pytest:**

    ```sh
    pytest test_project.py
    ```

    This will execute all the unit tests to ensure the functionality of the main application.

## Functions

### project.py

- `main()`: Main function that handles user interaction, including registration, login, and transaction options.
- `register_user(users, username, password)`: Registers a new user with a username and password.
- `login_user(users, username, password)`: Authenticates a user based on the username and password.
- `add_funds(user_data, amount)`: Adds a specified amount to the current balance and logs the transaction.
- `withdraw_funds(user_data, amount)`: Withdraws a specified amount from the current balance if sufficient funds are available and logs the transaction.
- `check_balance(user_data)`: Returns the current balance with the owner's name.
- `show_transaction_history(user_data)`: Displays all transactions for the user.
- `calculate_interest(user_data, rate, years)`: Calculates interest on the current balance over a given period.

### test_project.py

- `test_register_user()`: Tests the `register_user` function.
- `test_login_user()`: Tests the `login_user` function.
- `test_add_funds()`: Tests the `add_funds` function.
- `test_withdraw_funds()`: Tests the `withdraw_funds` function.
- `test_check_balance()`: Tests the `check_balance` function.
- `test_show_transaction_history()`: Tests the `show_transaction_history` function.
- `test_calculate_interest()`: Tests the `calculate_interest` function.



