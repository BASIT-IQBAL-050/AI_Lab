class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, customer_name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = self.Account(account_number, customer_name, initial_balance)
            print(f"Account {account_number} created for {customer_name} with initial balance {initial_balance}")
        else:
            print(f"Account {account_number} already exists")

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed")
        else:
            print(f"Account {account_number} does not exist")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            print(f"Deposited {amount} into account {account_number}")
        else:
            print(f"Account {account_number} does not exist")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].balance >= amount:
                self.accounts[account_number].withdraw(amount)
                print(f"Withdrew {amount} from account {account_number}")
            else:
                print(f"Insufficient balance in account {account_number}")
        else:
            print(f"Account {account_number} does not exist")

    class Account:
        def __init__(self, account_number, customer_name, initial_balance):
            self.account_number = account_number
            self.customer_name = customer_name
            self.balance = initial_balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount


# for checking if there is some error or not
bank = Bank()
bank.add_account(1001, "Alice", 1000)
bank.add_account(1002, "Bob", 500)
bank.deposit(1001, 200)
bank.withdraw(1002, 1000)
bank.remove_account(1001)


# now dynamically taking input from the user so that user can chose what action he wants to perfom
while True:
    print("Select the Option to perform the action: ")
    print("1. Add Account")
    print("2. Deposit")
    print("3. Withdraw  ")
    print("4. Remove Account  ")
    ch = int(input("Enter Your Choice : "))
    
    match ch:
        case 1:
            accNum = int(input("Enter the Account Number of : "))
            nameOfCustomer = input("Enter the Name of Owner of Account  : ")
            initialBalance = int(input("Enter inital Balance : "))
            
            bank.add_account(accNum, nameOfCustomer, initialBalance)
        case 2:
            accNum = int(input("Enter the Account Number : "))
            amount = int(input("Enter the amount You want to add : "))
            bank.deposit(accNum, amount)
        
        case 3:
            accNum = int(input("Enter the Account Number : "))
            amount = int(input("Enter the amount You want to withdraw : "))
            bank.withdraw(accNum, amount)
        
        case 4:
              accNum = int(input("Enter the account Number You want to remove : "))
              bank.remove_account(accNum)
        case _:
            print("invalid Input")
            
    choice = input("Would You like to exit (y) : ")
    if(choice in ['y', 'Y']):
        break
            

        


