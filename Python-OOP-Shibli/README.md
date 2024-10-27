# Coding Task for Validata Developers (Python)
# Part 1: Object-Oriented Programming
# Python OOP: Bank Account and Shopping Cart

This project demonstrates the use of Object-Oriented Programming (OOP) concepts in Python by implementing two classes: `BankAccount` and `ShoppingCart`. The `BankAccount` class simulates a basic bank account with operations like deposit, withdraw, and balance check, while the `ShoppingCart` class allows adding, removing items, and calculating the total cost of items in a shopping cart.

## Requirements
- Python 3.6 or higher

## Features

### BankAccount Class
The `BankAccount` class provides basic banking functionality, including:
- **Attributes:**
  - `account_number`: Unique identifier for the bank account.
  - `account_holder`: Name of the account holder.
  - `balance`: The current balance in the account.
- **Methods:**
  - `deposit(amount)`: Adds the specified amount to the balance.
  - `withdraw(amount)`: Deducts the specified amount from the balance if there are sufficient funds.
  - `check_balance()`: Returns the current balance.
  - `display_account_details()`: Prints the account details including account number, account holder name, and balance.

### ShoppingCart Class
The `ShoppingCart` class provides functionalities for managing a shopping cart:
- **Attributes:**
  - `cart_items`: Dictionary storing items and their prices.
  - `total_cost`: The total cost of all items in the cart.
- **Methods:**
  - `add_item(item_name, price)`: Adds an item and its price to the cart.
  - `remove_item(item_name)`: Removes an item from the cart if it exists.
  - `calculate_total_cost()`: Returns the total cost of items in the cart.
  - `display_cart_contents()`: Displays all items in the cart with their prices and the total cost.

## Getting Started

### Prerequisites
- Make sure Python is installed. [Download Python](https://www.python.org/downloads/)

### Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/MD-Shibli-Mollah/SH-Python-2024.git
   ```
2. Navigate to the project directory
```bash
    cd SH-Python-2024/Python-OOP-Shibli
```
## Usage
1. BankAccount Class Example
```bash
# Import the BankAccount class
from bank_account import BankAccount

# Create a new bank account
account = BankAccount("1141000000876", "MD Shibli Mollah", 500.0)

# Deposit money
account.deposit(100)   # New balance should be 600

# Withdraw money
account.withdraw(50)   # New balance should be 550

# Check balance
print(account.check_balance())  # Output: 550

# Display account details
account.display_account_details()
```

2. ShoppingCart Class Example
```bash
# Import the ShoppingCart class
from shopping_cart import ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Add items
cart.add_item("Apple", 1.2)
cart.add_item("Banana", 0.8)
cart.add_item("Milk", 3.5)

# Remove an item
cart.remove_item("Banana")

# Calculate total cost
print("Total Cost:", cart.calculate_total_cost())

# Display cart contents
cart.display_cart_contents()
```
## Testing
A separate test file (`test_app.py`) can be created to ensure that all CRUD operations for both classes are working correctly. Example tests could include adding/removing items in the `ShoppingCart` and depositing/withdrawing funds in `BankAccount`.
To run the tests:
```bash
python test_app.py
```
## Acknowledgments
This project is intended as a demonstration of basic OOP concepts in Python. It showcases class creation, encapsulation, and method definitions, providing a simple yet practical example for beginners.