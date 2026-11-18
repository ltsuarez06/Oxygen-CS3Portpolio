class LabEquipment:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def display_info(self):
        print("Lab Equipment Name:", self.name)
        print("Brand:", self.brand)

Lab1 = LabEquipment("Micrscope", "Ohaus")
Lab1.display_info()

class Microscope:
    def __init__(self, name, brand, magnification):
        self.name = name
        self.brand = brand
        self.magnification = magnification

    def view(self):
        print(f"Magnification: {self.magnification}")

    def display_full_info(self):
        print("Microscope Information:")
        print("Microscope Name:", self.name)
        print("Brand:", self.brand)
        print(f"Magnification: {self.magnification}")

mic1 = Microscope("Microscope", "Zeiss", "100x")
mic1.view()
mic1.display_full_info()