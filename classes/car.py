# Python Crash Course: Chapter 8, Eric Matthews, Classes

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Set a default value.
        self.odometer_reading = 0

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

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

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
