import json
from datetime import datetime  
class BankAccount:

    def __init__(self, account_number, balance=0, owner_name=''):
        self.account_number = account_number
        self.balance = balance 
        self.owner_name = owner_name

    @property
    def balance(self):
        return self._balance  
    
    @balance.setter
    def balance(self, value):
        """
        Setter for balance. Ensures balance cannot be set to a negative value.
        """
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value 
    
    @classmethod
    def dictBank(cls, data):
        return cls(data["account_number"], data["balance"], data["owner_name"]) 
    
    @staticmethod
    def checkAmount(amount):
        if amount <= 0:
            raise ValueError("Amount can't be negative or zero")
        return True
    
    def deposit(self, amount):
        if self.checkAmount(amount):
            self.balance += amount
            self.logTransaction(f"{amount} has been deposited")

    def withdraw(self, amount):
        if self.checkAmount(amount):
            if self.balance < amount:  # Corrected condition
                raise ValueError(f"{amount} cannot be withdrawn due to insufficient funds")
            self.balance -= amount
            self.logTransaction(f"{amount} has been withdrawn")
       
    def checkBalance(self):
        return self.balance
    
    def logTransaction(self, message):
        timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp
        print(f"[{timeStamp}] {message}")
    
    def __str__(self):
        yellow = "\033[93m"
        green = "\033[92m"
        orange = "\033[33m"
        reset = "\033[0m"

        return (
        f"Bank Account: "
        f"Account Number = {yellow}{self.account_number}{reset}, "
        f"Balance = {green}${self.balance}{reset}, "
        f"Owner Name = {orange}{self.owner_name}{reset}"
    )
    
    def saveToFile(self, filename):
        data = {
            "account_number": self.account_number,  # Consistent key names
            "balance": self.balance,
            "owner_name": self.owner_name,
        }
        
        with open(filename, "w") as file:  # Fixed typo
            json.dump(data, file)
    
    @classmethod
    def loadFromFile(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return cls.dictBank(data)

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456", 1000, "John Doe")
    account.deposit(500)
    account.withdraw(200)
    print(account.checkBalance())
    print(account)
    account.saveToFile("account_data.json")

    loaded_account = BankAccount.loadFromFile("account_data.json")
    print(loaded_account)