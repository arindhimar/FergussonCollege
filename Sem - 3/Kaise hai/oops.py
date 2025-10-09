from abc import ABC, abstractmethod

class Account:
    total_accounts = 0
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
        Account.total_accounts += 1
        
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def __str__(self):
        return f"Account {self.__account_number}: Balance {self.__balance}"
    
    
    
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate
        
    def deposit(self, amount):
        if amount > 0:
            self._Account__balance += amount
            print(f"Deposited {amount}. New balance is {self._Account__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self._Account__balance:
            self._Account__balance -= amount
            print(f"Withdrew {amount}. New balance is {self._Account__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def apply_interest(self):
        interest = self._Account__balance * self.__interest_rate
        self._Account__balance += interest
        print(f"Applied interest of {interest}. New balance is {self._Account__balance}.")

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.__overdraft_limit = overdraft_limit
        
    def deposit(self, amount):
        if amount > 0:
            self._Account__balance += amount
            print(f"Deposited {amount}. New balance is {self._Account__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self._Account__balance + self.__overdraft_limit:
            self._Account__balance -= amount
            print(f"Withdrew {amount}. New balance is {self._Account__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
    def get_overdraft_limit(self):
        return self.__overdraft_limit
    


class Bank:
    def __init__(self):
        self.accounts = {}
        
    def add_account(self, account):
        if account.get_account_number() not in self.accounts:
            self.accounts[account.get_account_number()] = account
            print(f"Account {account.get_account_number()} added.")
        else:
            print("Account already exists.")
    
    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed.")
        else:
            print("Account not found.")
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    
    def total_accounts(self):
        return len(self.accounts)

def menu():
    print("1. Create Savings Account")
    print("2. Create Checking Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Apply Interest (Savings Only)")
    print("6. View Account Balance")
    print("7. Exit")

if __name__ == "__main__":
    bank = Bank()
    
    while True:
        menu()
        
        opt = input("Choose an option:\n")
        if opt == '1':
            acc_num = input("Enter account number: ")
            initial_deposit = float(input("Enter initial deposit: "))
            interest_rate = float(input("Enter interest rate (default 0.02): ") or 0.02)
            account = SavingsAccount(acc_num, initial_deposit, interest_rate)
            bank.add_account(account)
        elif opt == '2':
            acc_num = input("Enter account number: ")
            initial_deposit = float(input("Enter initial deposit: "))
            overdraft_limit = float(input("Enter overdraft limit (default 500): ") or 500)
            account = CheckingAccount(acc_num, initial_deposit, overdraft_limit)
            bank.add_account(account)
        elif opt == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(acc_num)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif opt == '4':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(acc_num)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif opt == '5':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            else:
                print("Account not found or not a savings account.")
        elif opt == '6':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif opt == '7':
            print("Exiting...")
            break
    
    