# Python Crash Course: Chapter 8, Eric Matthews, Functions


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    """Positional argurment: animal_type (string), pet_name (string). Order dependent."""
    """Keyword argument: animal_type='value', pet_name='value'. Order independent."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def describe_pet_dog(animal_type, pet_name='dog'):
    """Display information about a pet where the average pet is a dog."""
    """Positional argurment: animal_type (string), pet_name (string). Order dependent."""
    """Keyword argument: animal_type='value', pet_name='value'. Order independent."""
    """Leaving out the pet_name, the function will still work."""
    """Note that the Positional arguments are listed before the default values"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Types of argumenets
# Positional arguments with multiple function calls.  The arguments must match the order of the parameters.
describe_pet('hamster', 'hairy')
describe_pet('dog', 'willie')
print("\nNot paying attention to order gives unexpected results!")
describe_pet('fluffy', 'hamster')

# Keyword arguments is a name_value pair passed to a function.
# argument=value.  Order is independent of the function variable order.

describe_pet(animal_type='hamster', pet_name='hairy')
describe_pet(pet_name='hairy', animal_type='hamster')

# Default values.  All of these functions work.
describe_pet_dog(animal_type='cat')
describe_pet_dog('willie')
describe_pet_dog('cat', 'fluffy')
describe_pet_dog(animal_type='cat', pet_name='fluffels')