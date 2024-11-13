# __init__.py
ADMIN_ROLE = 'Admin'
USER_ROLE = 'User'

users_db = {
    'admin': {'password': 'admin123', 'role': ADMIN_ROLE},
    'user': {'password': 'user123', 'role': USER_ROLE}
}

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, "
              f"Price: {self.price}, Stock: {self.stock_quantity}")

    def restock(self, amount):
        self.stock_quantity += amount
        print(f"Product '{self.name}' restocked by {amount}. New stock: {self.stock_quantity}")

    def reduce_stock(self, amount):
        if amount > self.stock_quantity:
            print(f"Cannot reduce {amount} units from '{self.name}'. Only {self.stock_quantity} in stock.")
        else:
            self.stock_quantity -= amount
            print(f"Product '{self.name}' reduced by {amount}. New stock: {self.stock_quantity}")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if any(prod.product_id == product.product_id for prod in self.products):
            print(f"Product with ID '{product.product_id}' already exists.")
        else:
            self.products.append(product)
            print(f"Product '{product.name}' added successfully.")

    def edit_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            try:
                product.name = input(f"Name [{product.name}]: ") or product.name
                product.category = input(f"Category [{product.category}]: ") or product.category
                price_input = input(f"Price [{product.price}]: ")
                product.price = float(price_input) if price_input else product.price
                stock_input = input(f"Stock Quantity [{product.stock_quantity}]: ")
                product.stock_quantity = int(stock_input) if stock_input else product.stock_quantity
                print(f"Product '{product_id}' updated successfully.")
            except ValueError:
                print("Invalid input. Price and Stock Quantity must be numbers.")
        else:
            print(f"Product with ID '{product_id}' not found.")

    def delete_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            self.products.remove(product)
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print(f"Product with ID '{product_id}' not found.")

    def view_products(self):
        print("\n=== View Products ===")
        if not self.products:
            print("No products available.")
        else:
            for prod in self.products:
                prod.display_product()
                if prod.stock_quantity < 5:
                    print("Warning: Stock is low. Consider restocking.")

    def search_products(self, search_term):
        results = [prod for prod in self.products if search_term.lower() in prod.name.lower() or
                   search_term.lower() in prod.category.lower()]
        if results:
            for prod in results:
                prod.display_product()
        else:
            print("No matching products found.")

    def adjust_stock(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            try:
                action = input("Enter 'restock' to increase or 'reduce' to decrease stock: ").lower()
                amount = int(input("Enter the amount: "))
                if action == 'restock':
                    product.restock(amount)
                elif action == 'reduce':
                    product.reduce_stock(amount)
                else:
                    print("Invalid action. Choose 'restock' or 'reduce'.")
            except ValueError:
                print("Invalid input. Amount must be a number.")
        else:
            print(f"Product with ID '{product_id}' not found.")

    def find_product_by_id(self, product_id):
        return next((prod for prod in self.products if prod.product_id == product_id), None)
