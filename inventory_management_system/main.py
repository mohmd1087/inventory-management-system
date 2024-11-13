# main.py

from __init__ import Product, Inventory, users_db, ADMIN_ROLE, USER_ROLE

def authenticate():
    print("=== Inventory Management System ===")
    username = input("Username: ")
    password = input("Password: ")

    user = users_db.get(username)
    if user and user['password'] == password:
        print(f"Login successful. Welcome, {username}!")
        return user['role']
    else:
        print("Invalid username or password.")
        return None


def display_menu(role):
    print("\n=== Main Menu ===")
    if role == ADMIN_ROLE:
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Search Products")
        print("6. Adjust Stock")
        print("7. Exit")
    else:
        print("1. View Products")
        print("2. Search Products")
        print("3. Exit")

def main():
    role = authenticate()
    if not role:
        return

    inventory = Inventory()

    while True:
        display_menu(role)
        choice = input("Select an option: ")
        if role == ADMIN_ROLE:
            if choice == '1':
                print("\n=== Add New Product ===")
                try:
                    product_id = input("Product ID: ")
                    name = input("Name: ")
                    category = input("Category: ")
                    price = float(input("Price: "))
                    stock_quantity = int(input("Stock Quantity: "))
                    product = Product(product_id, name, category, price, stock_quantity)
                    inventory.add_product(product)
                except ValueError:
                    print("Invalid input. Price and Stock Quantity must be numbers.")
            elif choice == '2':
                print("\n=== Edit Product ===")
                product_id = input("Enter the Product ID to edit: ")
                inventory.edit_product(product_id)
            elif choice == '3':
                print("\n=== Delete Product ===")
                product_id = input("Enter the Product ID to delete: ")
                inventory.delete_product(product_id)
            elif choice == '4':
                inventory.view_products()
            elif choice == '5':
                print("\n=== Search Products ===")
                search_term = input("Enter product name or category to search: ")
                inventory.search_products(search_term)
            elif choice == '6':
                print("\n=== Adjust Stock ===")
                product_id = input("Enter the Product ID to adjust stock: ")
                inventory.adjust_stock(product_id)
            elif choice == '7':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            if choice == '1':
                inventory.view_products()
            elif choice == '2':
                print("\n=== Search Products ===")
                search_term = input("Enter product name or category to search: ")
                inventory.search_products(search_term)
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
