# Python Crash Course: Chapter 8, Eric Matthews, Functions

# to get a specific function from a module:
# from module_name import function_name
# from module_name import function_0, function_1, function_2
from pizza_mod import make_pizza

# to get any function use the following syntax
# function_0()
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')