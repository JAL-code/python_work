# Python Crash Course: Chapter 8, Eric Matthews, Functions

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested.
    *variable will create an empty tuple and pack the values inside.
    Like default values, arbitrary arguments are listed after Positional parameters.
    arbitrary positional arguments: *args"""
    print("\n Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
