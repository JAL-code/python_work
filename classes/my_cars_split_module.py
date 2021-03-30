# Python Crash Course: Chapter 8, Eric Matthews, Classes

"""An example using the class Car and its subclasses."""
# This example uses a split version of the Car and ElectricCar classes.
# Also note that ElectricCar is aliased as EC.
from car_main import Car
from electric_car import ElectricCar as EC

my_beetle = Car('audi', 'a4', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())