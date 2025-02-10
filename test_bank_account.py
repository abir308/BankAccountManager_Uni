import pytest 
from bank_account import BankAccount

def test_deposit():
    account = BankAccount("123456", 1000, "John Doe")
    account.deposit(500)
    assert account.checkBalance() == 1500

def test_withdraw():
    account = BankAccount("123456", 1000, "John Doe")
    account.withdraw(200)
    assert account.checkBalance() == 800

def test_insufficient_funds():
    account = BankAccount("123456", 1000, "John Doe")
    with pytest.raises(ValueError):
        account.withdraw(1500)

def test_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("123456", -100, "John Doe")

def test_from_dict():
    data = {"account_number": "123456", "balance": 1000, "owner_name": "John Doe"}
    account = BankAccount.dictBank(data)
    assert account.account_number == "123456"
    assert account.balance == 1000
    assert account.owner_name == "John Doe"
