#-------------------Sari-Sari Store Inventory Management System----------------------
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, quantity):
        self.quantity -= quantity
        print(f"Sold {quantity} {self.name}")

    def restock(self, quantity):
        self.quantity += quantity
        print(f"Restocked {quantity} {self.name}")

    def display_info(self):
        print(f"{self.name} - Price: ₱{self.price}, Stock: {self.quantity}")


# --------------------------Testing the Product class--------------------------
item1 = Product("Soda", 20, 10)

item1.display_info()
item1.sell(3)
item1.display_info()
item1.restock(5)
item1.display_info()
