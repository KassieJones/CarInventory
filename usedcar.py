class Used_Car:
    def __init__(self, year, make, model, price, mileage):
        self.year = year
        self.make = make
        self.model = model
        self.price = price
        self.mileage = mileage

    def __str__(self):
        return f"{self.year}  -----  {self.make}  -----  {self.model}  -----  {self.price}  -----  {self.mileage}"

class Car:
    def __init__(self, year, make, model, price):
        self.year = year
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.year}  -----  {self.make}  -----  {self.model}   -----  {self.price}"


if __name__ == '__main__':
    cont = 'y'
    inventory = []

    print('Welcome to the Grand Circus admin console!')
    car_one = Car('2017', 'Nikolai', 'Model S ', '54,999.90')
    car_two = Car('2018', 'Fourd  ', 'Escapade', '31,900.00')
    car_three = Car('2018', 'Chewie ', "Vette   ", '44,989.95')
    car_four = Used_Car('2010', 'Hyonda ', 'Prior    ', '14,700.90', '35,987 miles')
    car_five = Used_Car('2014', 'GC     ', 'Chirpus  ', ' 8,500.00', '12,345 miles')
    car_six = Used_Car('2015', 'GC     ', 'Witherall', ' 8,500.00', '14,379 miles')

    inventory.append(car_one)
    inventory.append(car_two)
    inventory.append(car_three)
    inventory.append(car_four)
    inventory.append(car_five)
    inventory.append(car_six)
    inventory.append('Quit')

    while cont.lower() == 'y':
        print('%28s' % 'Car Inventory')
        counter = 0
        for i in inventory:
            counter = counter + 1
            print(str(counter) + '. ', end="")
            print(i)

        user_choice = int(input('Please enter the number of the car you would like:  '))
        if user_choice >=1 and user_choice < len(inventory)-1:
            print(inventory[user_choice-1])
            buy_car = input('Would you like to buy this car? y/n')
            if buy_car.lower() == 'y':
                inventory.__delitem__(user_choice-1)
                print('Excellent!  Our finance department will be in touch shortly.')
                cont = 'y'
            else:
                print('Returning you to the inventory list.')
        elif user_choice == len(inventory):
            print('Have a great day!')
            break
        else:
            print('Please enter a valid selection')
