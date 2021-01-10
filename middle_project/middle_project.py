# classes defined --------------------------------

class spacecraft:
    def __init__(self, id, name, speed, arm, capacity, ):
        self.id = id # unique ID (str)
        self.name = name # name of the ship (str)
        self.speed = speed # speed X light speeds (int)
        self. arm = arm # weapon power grade (1-10 int)
        self. capacity = capacity

class craftport:
    def __init__(self, name, address, products):
        self.name = name
        self.address = address
        self.products = products

jedi_starfighter = spacecraft("cr1","Jedi Starfigter", 5, 1, 3)