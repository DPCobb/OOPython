# Bicycle is an abstract class, it's attributes are shared by all types of bikes we create
# To avoid writing these attributes over and over we created an abstract class
class Bicycle(object):
    def __init__(self, model):
        self.wheels = 2
        self.max_speed = 15
        self.frame = 'aluminum'
        self.model = model

# MountainBike is a type of bike that builds on Bicycle
class MountainBike(Bicycle):
    def __init__(self, price, model):
        super(MountainBike, self).__init__(model)
        self.color = "Red"
        self.brakes = "Disc"
        self.seat_comfort = 5
        self.price = price

# Cruiser is a type of bike that builds on Bicycle
class Cruiser(Bicycle):
    def __init__(self, price, size, model):
        super(Cruiser, self).__init__(model)
        self.color = "Blue"
        self.brakes = "Pad"
        self.seat_comfort = 10
        self.price = price
        self.size = size

