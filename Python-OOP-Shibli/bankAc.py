class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        """
        Initializes a new bank account with the given account number, account holder's name,
        and an optional initial balance (default is 0.0).
        Parameters:
        - account_number (str): The account number of the bank account.
        - account_holder (str): The name of the account holder.
        - balance (float): The initial balance of the account. Defaults to 0.0.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance, provided it is positive.
        Parameters:
        - amount (float): The amount to deposit. Must be greater than 0.
        
        If the amount is valid, updates the balance and displays a success message.
        Otherwise, prints an error message.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposit is successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if sufficient funds are available.
        Parameters:
        - amount (float): The amount to withdraw. Must be greater than 0.

        Checks if the balance is enough for the withdrawal.
        If valid, deducts from the balance and prints a success message.
        If the balance is insufficient or the amount is invalid, prints an error message.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal is successful. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def check_balance(self):
        """
        Returns the current account balance.

        Returns:
        - balance (float): The current balance of the account.
        """
        return self.balance

    def display_account_details(self):
        """
        Displays account information, including account number, account holder's name, and balance.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Usage Example
# Create a new bank account instance with an initial balance of 500.0
account = BankAccount("1141000000876", "MD Shibli Mollah", 500.0)

# Perform a deposit of 100
account.deposit(100)  # Expected output: Deposit successful. New balance: 600.0

# Perform a withdrawal of 50
account.withdraw(50)  # Expected output: Withdrawal successful. New balance: 550.0

# Check and print the current balance
print(account.check_balance())  # Expected output: 550.0

# Display the account details
account.display_account_details()  
# Expected output:
# Account Number: 1141000000876
# Account Holder: MD Shibli Mollah
# Balance: 550.0