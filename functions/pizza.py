# Python Crash Course: Chapter 8, Eric Matthews, Functions

def make_pizza(*toppings):
    """Print the list of toppings that have been requested.
    *variable will create an empty tuple and pack the values inside."""
    print("\n Making a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
