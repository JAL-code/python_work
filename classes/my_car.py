# Python Crash Course: Chapter 8, Eric Matthews, Classes

"""An example using the class Car and its subclasses."""

from car import Car
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23
my_new_car.read_odometer()
