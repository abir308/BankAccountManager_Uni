import json
from datetime import datetime  
class BankAccount:

    def __init__(self, account_number, balance=0, owner_name=''):
       # Initialize the bank account with account number, balance, and owner name.
        self.account_number = account_number
        self.balance = balance     # Uses the setter to validate balance
        self.owner_name = owner_name

    @property
    def balance(self):
        # Get the balance
        return self._balance  
    
    @balance.setter
    def balance(self, value):
        # Set the balance, ensuring it is not negative
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value 
    
    @classmethod
    def dictBank(cls, data):
        # Create a BankAccount object from a dictionary
        return cls(data["account_number"], data["balance"], data["owner_name"]) 
    
    @staticmethod
    def checkAmount(amount):
        # Check if the amount is valid (greater than zero)
        if amount <= 0:
            raise ValueError("Amount can't be negative or zero")
        return True
    
    def deposit(self, amount):
        # Deposit money into the account
        if self.checkAmount(amount):    # Validates amount
            self.balance += amount     # Increase balance
            self.logTransaction(f"{amount} has been deposited")     # Logs transaction

    def withdraw(self, amount):
         # Withdraw money if there is enough balance
        if self.checkAmount(amount):    
            if self.balance < amount:   
                raise ValueError(f"{amount} cannot be withdrawn due to insufficient funds")
            self.balance -= amount    # Decrease balance
            self.logTransaction(f"{amount} has been withdrawn")    
       
    def checkBalance(self):
        # Return the current balance
        return self.balance
    
    def logTransaction(self, message):
        # Log the transaction with a timestamp
        timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        print(f"[{timeStamp}] {message}")
    
    def __str__(self):
        # Return a formatted string representation of the account
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
        # Save account details to a JSON file
        data = {
            "account_number": self.account_number,  # Consistent key names
            "balance": self.balance,
            "owner_name": self.owner_name,
        }
        
        with open(filename, "w") as file:  # Fixed typo
            json.dump(data, file)
    
    @classmethod
    def loadFromFile(cls, filename):
        # Load account details from a JSON file
        with open(filename, "r") as file:
            data = json.load(file)
        return cls.dictBank(data)

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456", 1000, "John Doe")    # Create an account
    account.deposit(500)    # Deposit money
    account.withdraw(200)    # Withdraw money
    print(account.checkBalance())    # Print balance
    print(account)    # Print account details
    account.saveToFile("account_data.json")    # Save account to a file

    loaded_account = BankAccount.loadFromFile("account_data.json")    # Load account from file
    print(loaded_account)    # Print loaded account details
