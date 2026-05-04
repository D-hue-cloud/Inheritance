class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(Vehicle):
    pass

School_bus=bus("School Volvo", 180, 12)

print("Vehicle name: ", School_bus.name, " | Speed: ", School_bus.maxspeed, " | Mileage: ", School_bus.mileage)
