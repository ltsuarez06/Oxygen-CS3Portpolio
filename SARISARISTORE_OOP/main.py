
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print("Price: ₱", self.price)
        print("Quantity:", self.quantity)

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} item(s).")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock.")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(f"Restocked {amount} item(s).")
            print(f"New quantity: {self.quantity}")

    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} item(s).")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock to remove that amount.")
def show_all_products(products_list):
    if not products_list:
        print("No products available.")
        return
    print("\n --- PRODUCT LIST --- ")
    print(f"{'No.':<4}{'Name':<30}{'Price':<10}{'Quantity':<8}")
    print(" -- " * 20)
    for i, p in enumerate(products_list, start=1):
        print(f"{i:<4}{p.name:<30}₱{p.price:<8}{p.quantity:<8}")


def search_product(products_list, name):
    for p in products_list:
        if p.name.lower() == name.lower():
            print(f"Find: {p.name} | Price: ₱{p.price} | Qty: {p.quantity}")
            return
    print(f"Product '{name}' not found.")


# Create product objects
products = []
product1 = Product("Lucky Me Pancit Canton", 15, 20)
product2 = Product("Coca-Cola", 25, 15)
product3 = Product("SkyFlakes", 10, 30)
product4 = Product("Piattos", 25, 12)
product5 = Product("Sardines", 30, 10)
products.extend([product1, product2, product3, product4, product5])


def show_menu():
    print("\n --- MENU --- ")
    print("1. Show All Products")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. Remove Product")
    print("5. Search Product")
    print("6. Exit")


if __name__ == "__main__":
    # use the initialized products list
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_all_products(products)

        elif choice == "2":
            name = input("Enter the product name to sell: ").strip()
            try:
                quantity = int(input("Enter the quantity to sell: ").strip())
            except ValueError:
                print("Invalid quantity. Must be a number.")
                input("Press Enter to continue...")
                continue
            for product in products:
                if product.name.lower() == name.lower():
                    product.sell(quantity)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "3":
            name = input("Enter the product name to restock: ").strip()
            try:
                amount = int(input("Enter the amount to restock: ").strip())
            except ValueError:
                print("Invalid amount. Must be a number.")
                input("Press Enter to continue...")
                continue
            for product in products:
                if product.name.lower() == name.lower():
                    product.restock(amount)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "4":
            name = input("Enter the product name to remove: ").strip()
            try:
                amount = int(input("Enter the amount to remove: ").strip())
            except ValueError:
                print("Invalid amount. Must be a number.")
                input("Press Enter to continue...")
                continue
            for product in products:
                if product.name.lower() == name.lower():
                    product.remove(amount)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "5":
            name = input("Enter the product name to search: ").strip()
            search_product(products, name)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")