class Car:
    def __init__(self, brand, model, age, average_speed):
        self.brand = brand
        self.model = model
        self.age = age
        self.average_speed = average_speed

    def time_calculator(self, distance, print_result=False):
        time = distance / self.average_speed
        if print_result:
            print(f'Time needed to cover {distance} km with model _ {self.model} is {round(time, 2)} hours.')
        else:
            return time


def compare(car1, car2):
    if car1.time_calculator(300) < car2.time_calculator(300):
        print(f'{car1.brand} is faster car')
    elif car2.time_calculator(300) < car1.time_calculator(300):
        print(f'{car2.brand} is faster car')
    else:
        print("There is not enough data for comparison")


car_1 = Car('Mercedes', 'S', 6, 120)
car_2 = Car('BMW', 'X5', 4, 160)

car_1.time_calculator(400, print_result=True)

compare(car_1, car_2)
