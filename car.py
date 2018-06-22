class Car:
    def __init__(self, year, make, model, price):
        self.year = year
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.year}        {self.make}      {self.model}       {self.price}"


if __name__ == '__main__':
    cont = 'y'
    inventory = []

    print('Welcome to the Grand Circus admin console!')

    number = int(input('How many cars are you entering?  '))

    for i in range(number):
        car_year = input('Year: ')
        car_make = input('Make: ')
        car_model = input('Model: ')
        car_price = input('Price:  ')

        car = Car (car_year, car_make, car_model, car_price)
        inventory.append(car)

    print('%25s' % 'Car Inventory')

    for i in inventory:
        print(i)

