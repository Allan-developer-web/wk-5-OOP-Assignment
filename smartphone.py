# Assignment 1: Design Your Own Class! 🏗️

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulated attribute

    def get_storage(self):
        return self._storage

    def set_storage(self, storage):
        if storage > 0:
            self._storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def __str__(self):
        return f"{self.brand} {self.model} ({self._storage}GB)"

# Inheritance: A subclass for a specific smartphone type
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

    def __str__(self):
        return f"{super().__str__()} - GPU: {self.gpu}"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 128)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, "Adreno 660")

    print(phone)
    phone.call("123-456-7890")

    print(gaming_phone)
    gaming_phone.play_game("PUBG Mobile")