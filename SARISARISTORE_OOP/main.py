class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

        def sell(self, quantity):
            if quantity <= self.quantity:
                self.quantity -= quantity
                print(f"Sold {quantity} item(s).")
                print(F"New Quantity: {self.quantity}")

            else:
                print("Not enough stock.") 

                def restock(self, amount):
                    if amount > 0:
                        print("Amount Must be Greater than 0.")

                    else:
                        self.quantity += amount
                        print(f"Restocked {amount} item(s).")
                        print(f"New Quantity: {self.quantity}")

                        #create an objedct

                        product1 = product("Lucky Me Pancit Canton", 15, 10)
                        print(product1.display_info())
                        print("--- Restocking 10 items ---")
                        product1.restock(10)
                        print("--- after Restocking ---")
                        product1.display_info()

                        def remove(self, amount):
                            if amount <= 0:
                                print("Amount must be greater than 0.") 
                            elif amount > self.quantity:
                                print("Not enough stock to remove.")
                                self.quantity -= amount
                                print(f"Removed {amount} item(s). new Quantity: {self.quantity}") 
                            else:
                                print("not enough stock to remove.")