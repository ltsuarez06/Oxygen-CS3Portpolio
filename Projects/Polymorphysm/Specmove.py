class PhysicsInstrument:
    def __init__(self, name, measurement):
        self.name = name
        self.__measurement = measurement

    @property
    def get_measurement(self):
        return self.__measurement

class Thermometer(PhysicsInstrument):
    def __init__(self, name, measurement, unit):
        super().__init__(name, measurement)

    def temp_interpret(self):
        if self.get_measurement < 20:
            return "Cool Temperature"
        elif 20 <= self.get_measurement < 30:
            return "Normal Temperature"
        else:
            return "High Temperature"

    def display_info(self):
        print(f"{self.name} Temperature Reading: {self.get_measurement}°C")
        print(f"Interpretation: {self.temp_interpret()}")

class Speedometer(PhysicsInstrument):
    def __init__(self, name, measurement, distance, time):
        super().__init__(name, measurement)
        self.distance = distance
        self.time = time

    def time_val(self):
        if self.time <= 0:
            raise ValueError("Invalid Time! Please enter a value greater than zero.")
        else:
            return self.time

    def speed(self):
        return self.distance / self.time_val()

    def display_info(self):
            print(f"{self.name}")
            print(f"Distance: {self.distance} km")
            print(f"Time: {self.time} hours")
            print(f"Speed: {self.speed()} km/h")

class ForceMeter(PhysicsInstrument):
    def __init__(self, name, measurement, mass, acceleration):
        super().__init__(name, measurement)
        self.mass = mass
        self.acceleration = acceleration

    def force(self):
        return self.mass * self.acceleration

    def display_info(self):
        print(f"{self.name}")
        print(f"Mass: {self.mass} kg")
        print(f"Acceleration: {self.acceleration} m/s^2")
        print(f"Force: {self.force()} N")

def display_readings(instrument):
    instrument.display_info()

thermo = float(input("Temperature in Celsius: "))
distance = float(input("Distance in kilometers: "))
time = float(input("Time in hours: "))
mass = float(input("Mass in kilograms: "))
acceleration = float(input("Acceleration in m/s^2: "))

thermometer = Thermometer("Thermometer", thermo, "Celsius")
speedometer = Speedometer("Speedometer", 0, distance, time)
force_meter = ForceMeter("Force Meter", 0, mass, acceleration)

instruments = [thermometer, speedometer, force_meter]

for instrument in instruments:
    display_readings(instrument)

print("END OF LABORATORY REPORT")
    




    

        

    
