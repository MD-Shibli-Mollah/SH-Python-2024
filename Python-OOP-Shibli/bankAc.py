class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        """Deducts the specified amount from the account balance if funds are sufficient."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def check_balance(self):
        """Returns the current account balance."""
        return self.balance

    def display_account_details(self):
        """Displays the account number, account holder, and current balance."""
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Create a new bank account
account = BankAccount("123456789", "John Doe", 500.0)

# Perform some transactions
account.deposit(100)         # Deposit 100
account.withdraw(50)         # Withdraw 50
print(account.check_balance()) # Check balance
account.display_account_details()  # Display account details
