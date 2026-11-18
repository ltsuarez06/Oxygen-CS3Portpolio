class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

   
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


    @property
    def bill_amount(self):
        return self.__bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if value < 0:
            raise ValueError("Bill cannot be negative.")
        self.__bill_amount = value

    @bill_amount.deleter
    def bill_amount(self):
        del self.__bill_amount

    def calculate_bill(self):
        return self.bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85



regular = Patient("Juan Dela Cruz", 15000)
senior = SeniorPatient("Maria Santos", 15000)
philhealth = PhilHealthPatient("Jose Rizal", 15000)


for patient in [regular, senior, philhealth]:
    print("Patient:", patient.name)
    print("Original Bill: ₱", patient.bill_amount)
    print("Final Bill: ₱", patient.calculate_bill())
    print("-" * 30)
