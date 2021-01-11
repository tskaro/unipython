# classes defined --------------------------------

class spacecraft:
    def __init__(self, name, speed, arm, capacity, quantity):
        self.name = name  # name of the ship (str)
        self.speed = speed  # speed X light speeds (int)
        self.arm = arm  # weapon power grade (1-10 int)
        self.capacity = capacity  # crew capacity (int)
        self.quantity = quantity  # number of items (int)


class craftport:
    def __init__(self, portname, address, products):
        self.portname = portname
        self.address = address
        self.products = products

    def menu(self):
        print('Welcome in Foundations intergalactic port, here is our legendary assortment:')
        for product in self.products:
            print(f'{product.name} with light speed of {product.speed}, weapon on a bord rank {product.arm},'
                  f' total capicity of {product.capacity} people. We have {product.quantity} left of those')


# spacecraft list---------------------------------

foundations_intergalactic_port = craftport("Foundations intergalactic port", "Canis Major Overdensity", [])
craft_list = [
    {"name": "Jedi Starfighter", "speed": 1, "arm": 1, "capacity": 15, "quantity": 11},
    {"name": "Starship Enterprise", "speed": 15, "arm": 9, "capacity": 3000, "quantity": 6},
    {"name": "Millennium Falcon", "speed": 18, "arm": 10, "capacity": 10, "quantity": 8},
    {"name": "super galaxy gurren lagann", "speed": 30, "arm": 10, "capacity": 10000, "quantity": 1}
]

for item in craft_list:
    name, speed, arm, capacity, quantity = item.values()
    foundations_intergalactic_port.products.append(spacecraft(name, speed, arm, capacity, quantity))

#print(foundations_intergalactic_port.products[1].arm)
print(foundations_intergalactic_port.menu())