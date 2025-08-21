class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"{self.name}: Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name}: Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name}: Sailing 🚤")

# Example usage
if __name__ == "__main__":
    car = Car("Toyota Corolla")
    plane = Plane("Boeing 747")
    boat = Boat("Sunseeker Yacht")

    vehicles = [car, plane, boat]
    for v in vehicles:
        v.move()