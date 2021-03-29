# Python Crash Course: Chapter 8, Eric Matthews, Functions

# PEP 8 - style coding (79 characters max)
# No spaces for default values
# After last ',' return a new line with second indent.
# Add a commit for all functions with 3 quotes per docstring format.
# import lines at start of program.
# descriptive names, lowercase letter and underscores
def make_pizza(
        size, *toppings):
    """Print the list of toppings that have been requested.
    *variable will create an empty tuple and pack the values inside.
    Like default values, arbitrary arguments are listed after Positional parameters.
    arbitrary positional arguments: *args"""
    print("\n Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")