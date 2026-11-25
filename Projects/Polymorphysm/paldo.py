class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

vehicles = [car1, boat1, drone1]

for vehicle in vehicles:
    start_trip(vehicle)

#How does the code in 2.2 demonstrate polymorphism
#The code in 2.2 demonstrates polymorphism through the use of a common interface (the `move` method) 
# across different classes (`Car`, `Boat`, and `Drone`). Each class implements the `move` method 
# in its own way, allowing objects of different types to be treated uniformly.