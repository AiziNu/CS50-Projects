import pytest
from project import add_funds, withdraw_funds, check_balance

def test_add_funds():
    assert add_funds(100, 50) == 150
    assert add_funds(0, 100) == 100
    assert add_funds(200, 0) == 200

def test_withdraw_funds():
    assert withdraw_funds(100, 50) == (50, "$50 withdrawn successfully.")
    assert withdraw_funds(100, 150) == (100, "Insufficient funds.")
    assert withdraw_funds(0, 50) == (0, "Insufficient funds.")

def test_check_balance():
    assert check_balance("Alice", 100) == "Alice's current balance: $100"
    assert check_balance("Bob", 0) == "Bob's current balance: $0"
    assert check_balance("Charlie", 150) == "Charlie's current balance: $150"

if __name__ == "__main__":
    pytest.main()
