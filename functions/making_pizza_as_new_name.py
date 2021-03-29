# Python Crash Course: Chapter 8, Eric Matthews, Functions

# to rename a specific function from a module:
# from module_name import function_name as fn
# from module_name import function_0 as fn0, function_1 as fn1, function_2 as fn2
from pizza_mod import make_pizza as mp

# to get any function use the following syntax
# fn0()
mp(16,'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')