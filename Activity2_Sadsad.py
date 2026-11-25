class Vehicle:
    alive = True

class Car(Vehicle):
    def move(self):
        print ("Cars can move on roads.")

class boat(Vehicle):
    def move(self):
        print ("The boat sails on water.")

class drone(Vehicle):
    def move(self):
        print ("The drone flies in the sky.")

vechicles = [Car(), boat(), drone()]

for vehicle in vechicles:
    vehicle.move()
    print(vehicle.move)


#Duck Typing is another way to implement polymorphism. It is a concept in programming that allows objects of different classes to be treated as if they were of the same class, based on their behavior rather than their actual type. In duck typing, an object's suitability for a particular use is determined by the presence of certain methods and properties, rather than its inheritance from a specific class.
#The car class inherits the move method from the vehicle class, but it also has its own implementation of the move method. The boat and drone classes also inherit the move method from the vehicle class, but they have their own implementations of the move method as well. This allows us to treat all three classes as if they were of the same type (i.e., they can all move), even though they are different classes with different implementations of the move method.