# Python Crash Course: Chapter 8, Eric Matthews, Classes

"""An example using the class Car and its subclasses."""

import car
my_tesla = car.ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_new_car = car.Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())