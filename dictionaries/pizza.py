# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
     }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
     "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
