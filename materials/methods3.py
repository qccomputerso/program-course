class Vehicle:
    def __init__(self, name, color, max_speed, brand):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.brand = brand
        self.type = "Unspecified"

class FancyVehicle(Vehicle):
    pass

class Lorry(Vehicle):
    def __init__(self, name, color, max_speed, brand):
        super().init(name, color, max_speed, brand)
        self.type = "Lorry"

class Car(Vehicle):
    def __init__(self, name, color, max_speed, brand):
        Vehicle.init(self, name, color, max_speed, brand)
        self.type = "Car"

weirdVehicle = FancyVehicle("weirdVehicle", "Black", 100, "Honda")
# name: "weirdVehicle", color: "Black", max_speed: 100, brand: "Honda", type: "Unspecified"

truck = Lorry("truck", "White", 130, "Toyota")
# name: "truck", color: "White", max_speed: 130, brand: "Toyota", type: "Lorry"

taxi = Car("taxi", "Red", 140, "Toyota")
# name: "taxi", color: "Red", max_speed: 140, brand: "Toyota", type: "Car"

# https://www.w3schools.com/python/python_inheritance.asp
# https://docs.python.org/3/tutorial/classes.html