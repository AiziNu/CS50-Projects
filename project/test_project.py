import pytest
from project import (
    register_user, login_user, add_funds, withdraw_funds,
    check_balance, show_transaction_history, calculate_interest
)

def test_register_user():
    users = {}
    register_user(users, 'testuser', 'password')
    assert 'testuser' in users
    assert users['testuser']['name'] == 'testuser'
    assert users['testuser']['password'] == 'password'

def test_login_user():
    users = {'testuser': {'name': 'testuser', 'password': 'password', 'balance': 0.0, 'transactions': []}}
    assert login_user(users, 'testuser', 'password') == users['testuser']
    assert login_user(users, 'testuser', 'wrongpassword') is None
    assert login_user(users, 'nonexistentuser', 'password') is None

def test_add_funds():
    user_data = {'name': 'testuser', 'balance': 100, 'transactions': []}
    add_funds(user_data, 50)
    assert user_data['balance'] == 150
    assert len(user_data['transactions']) == 1
    assert user_data['transactions'][0][1] == 'Deposit'
    assert user_data['transactions'][0][2] == 50

def test_withdraw_funds():
    user_data = {'name': 'testuser', 'balance': 100, 'transactions': []}
    balance, message = withdraw_funds(user_data, 50)
    assert balance == 50
    assert message == "$50 withdrawn successfully."
    assert len(user_data['transactions']) == 1
    assert user_data['transactions'][0][1] == 'Withdraw'
    assert user_data['transactions'][0][2] == 50
    balance, message = withdraw_funds(user_data, 200)
    assert balance == 50
    assert message == "Insufficient funds."

def test_check_balance():
    user_data = {'name': 'testuser', 'balance': 100}
    assert check_balance(user_data) == "testuser's current balance: $100"

def test_show_transaction_history(capfd):
    user_data = {'name': 'testuser', 'balance': 100, 'transactions': []}
    show_transaction_history(user_data)
    out, err = capfd.readouterr()
    assert out.strip() == "No transactions found."

    user_data['transactions'].append((datetime.datetime.now(), 'Deposit', 50))
    show_transaction_history(user_data)
    out, err = capfd.readouterr()
    assert "Transaction history:" in out
    assert "Deposit: $50" in out

def test_calculate_interest():
    user_data = {'name': 'testuser', 'balance': 100}
    assert calculate_interest(user_data, 5, 2) == 10

if __name__ == "__main__":
    pytest.main()

