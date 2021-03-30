# Python Crash Course: Chapter 8, Eric Matthews, Classes

# Class Car is parent class.  It must appear before the child classes.
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Set a default value.
        self.odometer_reading = 0
        # Set the warning level for gas refill
        self.gas_refill = 450
        self.max_range = 500

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
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
        print("Go get some gas! Your tank is low.")

class ElectricCar(Car):
    "represents aspects of a car, specific to electric vehicles."""
    #  This class will inherit the attributes and methods of
    #  an car and then additional characterics.

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class (car)."""
        # super() calls methods from the parent class.
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """ Electric cars do not have gas tanks. """
        print("This car does not need a gas tank.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Assign some mileage to the odometer.
# Access the attribute through self and assign the value with =.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Another option is to add a method that updates the value for you.
my_new_car.update_odometer(64)
my_new_car.read_odometer()

#  Use the increment_odometer and update_odometer methods.
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Attempt to rollback the odometer
my_used_car.update_odometer(20_000)
my_used_car.read_odometer()

# Let us expand the Car class as a parent of the Electric Car class.
print("\nTime to make some electric cars!")
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Using the fact that electric cars do not have gas tanks
# create a function to warn the owner when the gas tank
# is low when updating the increment_odometer function.

my_tesla.increment_odometer(300)
my_tesla.read_odometer()

my_tesla.increment_odometer(356)
my_tesla.read_odometer()

my_tesla.increment_odometer(475)
my_tesla.read_odometer()