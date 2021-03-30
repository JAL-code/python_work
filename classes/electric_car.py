# Python Crash Course: Chapter 8, Eric Matthews, Classes

from car_main import Car
"""A class that can be used to represent an electric car."""

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        if not battery_size:
            print(f"Test: {battery_size}")
            self.battery_size = 75
        else:
            self.battery_size = battery_size

    def set_battery_size(self, size):
        self.battery_size = size
        self.describe_battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    "represents aspects of a car, specific to electric vehicles."""
    #  This class will inherit the attributes and methods of
    #  an car and then additional characterics.

    def __init__(self, make, model, year, battery_size=''):
        """Initialize attributes of the parent class (car)."""
        # super() calls methods from the parent class.
        super().__init__(make, model, year)
        # Replace this line --> self.battery_size = 75 <-- with the
        # following line to create a Battery object.
        # The object is an attribute of the electric car.
        # The command also creates the instance of a battery
        # associated with the electric car.
        if battery_size:
            self.battery = Battery(battery_size)
        if not battery_size:
            self.battery = Battery()

    def fill_gas_tank(self):
        """ Electric cars do not have gas tanks. """
        print("This car does not need a gas tank.")