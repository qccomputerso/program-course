class Vehicles:

    def __init__(self, name, color, max_speed, brand):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.brand = brand

    
class Lorry(Vehicles):
    pass

class Car(Vehicles):
    pass


Truck = Lorry('Trucks', 'White', 130, 'Toyota')

Taxi = Car('Taxi', 'Red', 140, 'Toyota')

print(Truck.name, Truck.color, Truck.max_speed, Truck.brand)




