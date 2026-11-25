print("===== WELCOME MINI STORE POS ODERING SYSTEM =====")

print("--- Product Menu ---")
print("1. Burger - PHP 50.00")
print("2. Fries - PHP 35.00")
print("3. Soft Drink - PHP 25.00")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

price1 = 50
price2 = 35
price3 = 25

Product1 = Product("Burger", price1)
Product2 = Product("Fries", price2)
Product3 = Product("Soft Drink", price3)


ProductNumber1 = input("Enter a Product Number(1-3): ")
ProductName1 = ""
if ProductNumber1 == "1":
    ProductName = Product1.name
elif ProductNumber1 == "2":
    ProductName = Product2.name
elif ProductNumber1 == "3":
    ProductName = Product3.name
Quantity1 = input("Enter Quantity: ")
Added = print("Added: " + str(ProductName) + " x " + str(Quantity1))


continue_ordering = input("Do you want to add another product? (yes/no): ")
if continue_ordering.lower() == "yes":
    ProductNumber2 = input("Enter a Product Number(1-3): ")
ProductName2 = ""
if ProductNumber2 == "1":
    ProductName = Product1.name
elif ProductNumber2 == "2":
    ProductName = Product2.name
elif ProductNumber2 == "3":
    ProductName = Product3.name
Quantity2 = input("Enter Quantity: ")
Added = print("Added: " + str(ProductName) + " x " + str(Quantity2))

continue_ordering = input("Do you want to add another product? (yes/no): ")
if continue_ordering.lower() == "yes":
    ProductNumber3 = input("Enter a Product Number(1-3): ")
ProductName3 = ""
if ProductNumber3 == "1":
    ProductName = Product1.name
elif ProductNumber3 == "2":
    ProductName = Product2.name
elif ProductNumber3 == "3":
    ProductName = Product3.name
Quantity3 = input("Enter Quantity: ")
Added = print("Added: " + str(ProductName) + " x " + str(Quantity3))

continue_ordering = input("Do you want to add another product? (yes/no): ")
if continue_ordering.lower() =="no":
    print("You may proceed to get the receipt")


Receipt = print("===== RECEIPT MINI STORE =====")

print("Product   Qty    Price   Subtotal")
print(ProductName1, Quantity1, price1, Quantity1 * price1 )
print(ProductName2, Quantity2, )


