class Customer:
    def __init__(self, OriginalBill):
        # Store in private variables with an underscore
        self._OriginalBill = OriginalBill
        self._Discount = 0.0
        self._NewBill = OriginalBill
        
        # Calculate discount and final bill on creation
        self.calculate_discount()

    # Property for OriginalBill
    @property
    def OriginalBill(self):
        return self._OriginalBill

    @OriginalBill.setter
    def OriginalBill(self, value):
        if value >= 0:
            self._OriginalBill = value
            # Recalculate bill whenever OriginalBill changes
            self.calculate_discount()

    # Property for Discount
    @property
    def Discount(self):
        return self._Discount

    # Property for NewBill
    @property
    def NewBill(self):
        return self._NewBill

    # Method to calculate discount and update NewBill
    def calculate_discount(self):
        if self._OriginalBill > 100:
            self._Discount = self._OriginalBill * 0.90
            
        # New bill is Original bill minus Discount
        self._NewBill = self._OriginalBill - self._Discount


# Instantiate the customer object (outside the class)
customer1 = Customer(150)

# Print output
print(f"Original Bill: ₱{customer1.OriginalBill:.2f}")
print(f"Discount: ₱{customer1.Discount:.2f}")
print(f"New Bill: ₱{customer1.NewBill:.2f}")