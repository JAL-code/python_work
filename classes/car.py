# Python Crash Course: Chapter 8, Eric Matthews, Classes
# JAL-code:
# - GasTank class
# - fill_gas_tank
# - assign electric battery_size from creation of ElectricCar

# Class Car is parent class.  It must appear before the child classes.
class Car:
    """A simple attempt to represent a car."""

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

#Use the default 500 mile range.
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.tank.describe_tank()
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

my_used_car.increment_odometer(450)
my_used_car.read_odometer()

# Attempt to rollback the odometer
my_used_car.update_odometer(20_000)
my_used_car.read_odometer()

# Let us expand the Car class as a parent of the Electric Car class.
print("\nTime to make some electric cars!")
print("Create the electric car with default battery")
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
#look at the my_tesla object, get attribute battery, call method describe_battery
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("Wrong battery size!")
my_tesla.battery.set_battery_size(100)

print("Create the electric car with 100 kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', '2019', battery_size=100)
my_tesla.battery.describe_battery()

# Using the fact that electric cars do not have gas tanks
# create a function to warn the owner when the gas tank
# is low when updating the increment_odometer function.
