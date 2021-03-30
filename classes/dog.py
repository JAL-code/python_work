# Python Crash Course: Chapter 8, Eric Matthews, Classes

class Dog:
    """A simple attempt to model a dog."""
    # The following functions are methods.
    # Init must be first in list of methods.
    # __init__ <-- syntax required to initialize the class.
    def  __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        # self gives access to the sit method to name and age.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Example code
my_dog = Dog('Daisy', 7)

print(f"My dog's name is {my_dog.name}. ")
print(f"My dog is {my_dog.age} years old.")

# Tell the dog to do something.
my_dog.sit()
my_dog.roll_over()

# Example code
print("\nCreate multiple instances")
my_dog = Dog('Dot', 7)
your_dog = Dog('Duke', 2)

print(f"My dog's name is {my_dog.name}. ")
print(f"My dog is {my_dog.age} years old.")
# Tell the dog to do something.
my_dog.sit()

print(f"Your dog's name is {your_dog.name}. ")
print(f"Your dog is {your_dog.age} years old.")
# Tell the dog to do something.
your_dog.sit()