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

    def assortment(self):
        for index, product in enumerate(self.products):
            print(
                f'{index + 1}. {product.name} with light speed of {product.speed}, weapon on a bord rank {product.arm},'
                f' total capicity of {product.capacity} people. We have {product.quantity} left of those')

    def check_quantity(self, index, number):  # Checks for products quantity in port
        return self.products[index - 1].quantity >= number

    def sell(self, index, number):  # Making correction of quantity after selling
        self.products[index - 1].quantity = self.products[index - 1].quantity - number

    def add_quantity(self, index, number):  # adds quantity of the product by number
        self.products[index - 1].quantity = self.products[index - 1].quantity + number


# spacecraft list---------------------------------------

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

# commend line ------------------------------------------

print('Oh who we got here?! Rick Sanchez! \n'
      'Welcome in Foundations intergalactic port,\n'
      'Here is our legendary assortment:')
foundations_intergalactic_port.assortment()
print('In which ship are you interested?')

while True:
    ship_index = int(input("Type the number of the ship:"))
    if ship_index <= len(foundations_intergalactic_port.products):
        print(f'{foundations_intergalactic_port.products[ship_index-1].name}?! Nice choice! \n'
              f'I have heard about your spectacular taste')
        break
    else:
        print("Please enter valid number")

while True:
    ship_quantity = int(input("How many ships you want to buy?"))
    if foundations_intergalactic_port.check_quantity(ship_index,ship_quantity) and ship_quantity > 0:
        foundations_intergalactic_port.sell(ship_index,ship_quantity)
        break
    else:
        print(f"Ohh... We don't have that many {foundations_intergalactic_port.products[ship_index-1].name}s\n"
              f"Please enter other quantity")

print(f'Menu after selling')
print(foundations_intergalactic_port.assortment())