import json
import datetime

class BankAccount:

    def __init__(self,  account_number, balance=0, owner_name=''):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    @property
    def balance(self):
        return self.balance
    

    @balance.setter
    def balance(self, value):
        
        if value <0:
            raise ValueError("Balance cant be negative")
        self.balance = value
    
    @classmethod
    def dictBank(cls, data):
        return cls(data["account_number"], data["balance"], data["owner_name"]) 
    
    @staticmethod
    def checkAmount(amount):
        if amount <=0:
            raise ValueError("Amount cant be negative")
        return True
    
    
    def deposit(self, amount):
        if self.checkAmount(amount):
            self.balance += amount
            self.logTransaction(f"{amount} has been deposited")

    def withdraw(self, amount):
        if self.checkAmount(amount):
            if self.balance <= amount:
                raise ValueError(f"{amount} cannot be withdrawed due to insufficient funds")
            self.balance -= amount
            self.logTransaction(f"{amount} has been withdrawn")
       
    def checkBalance(self):
        return self.balance
    
    def logTransaction(self, message):

        timeStamp = datetime.now()
        print(f"[{timeStamp}] {message}")
    
    def __str__(self):
        return f"Bank Account: Account Number = {self.account_number}, Balence= ${self.balance}, Owner Name = {self.owner_name}"
