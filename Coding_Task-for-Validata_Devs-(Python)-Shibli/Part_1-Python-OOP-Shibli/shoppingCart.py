class ShoppingCart:
    def __init__(self):
        self.cart_items = {}  # Dictionary to store items with their prices
        self.total_cost = 0.0 # Initialize total cost

    def add_item(self, item_name, price):
        """Adds an item and its price to the cart."""
        if price > 0:
            self.cart_items[item_name] = self.cart_items.get(item_name, 0) + price
            self.total_cost += price
            print(f"{item_name} is added to the cart. Current total: {self.total_cost}")
        else:
            print("Invalid price. Please enter a positive amount.")

    def remove_item(self, item_name):
        """Removes an item from the cart if it exists."""
        if item_name in self.cart_items:
            self.total_cost -= self.cart_items.pop(item_name)
            print(f"{item_name} is removed from the cart. Current total: {self.total_cost}")
        else:
            print(f"{item_name} not found in cart.")

    def calculate_total_cost(self):
        """Returns the total cost of the items in the cart."""
        return self.total_cost

    def display_cart_contents(self):
        """Displays each item in the cart with its price."""
        print("Cart Contents:")
        for item, price in self.cart_items.items():
            print(f"{item}: ${price}")
        print(f"Total Cost: ${self.total_cost}")

# Create a new shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apple", 1.2)      # Add an Apple with price 1.2
cart.add_item("Banana", 0.8)     # Add a Banana with price 0.8
cart.add_item("Milk", 3.5)       # Add Milk with price 3.5

# Remove an item from the cart
cart.remove_item("Banana")

# Calculate total cost and display contents
print("Total Cost:", cart.calculate_total_cost())
cart.display_cart_contents()
