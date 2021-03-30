# Python Crash Course: Chapter 8, Eric Matthews, Classes

"""An example using the class Car and its subclasses."""

from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()