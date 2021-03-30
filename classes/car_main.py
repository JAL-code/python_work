# Python Crash Course: Chapter 8, Eric Matthews, Classes
#

"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car with a gas tank."""

    def __init__(self, make, model, year, mpg=20, range=500):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Set a default value.
        self.odometer_reading = 0
        # Set the warning level for gas refill
        self.gas_refill = .8*range
        self.max_range = range
        self.mpg = mpg
        self.tank = GasTank(volumetric_size=(range/mpg))

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"Your car:{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        # If a method has a print output, don't print the method.
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the mileage.")

    def update_max_range(self, refill, max_range):
        """refill: Set the warning for when tank needs to be refilled.
        max_range: Set the maximum range of the car.
        """
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the mileage.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.
        This method can used to track weekly mileage."""
        self.odometer_reading += miles
        if miles >= self.gas_refill and miles < self.max_range:
            self.fill_gas_tank()

    def fill_gas_tank(self):
        """ Warns the owner to get some gas if mileage added is
        greated than 300 miles. """
        print("Go, get some gas! Your tank is low.")


class GasTank:
    """A simple class to represent a gas tank for cars."""
    def __init__(self, volumetric_size=10, units='gallon'):
        """Initialize attributes of the parent class (car)."""
        self.volumetric_size = volumetric_size
        self.units = units

    def set_tank_size(self, volumetric_size, units):
        self.volumetric_size = volumetric_size
        self.units = gallons

    def describe_tank(self):
        """Print a statement describing the tank size."""
        print(f"This car has a {self.volumetric_size}-{self.units} tank.")