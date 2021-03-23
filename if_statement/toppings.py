# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Window 10

#test for inequality or "not"
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#check if value is in a list?
requested_topping = ['mushrooms', 'onions', 'pineapple']
print(requested_topping)
print(f"Mushrooms: {'mushrooms' in requested_topping}.")
print(f"Pepperoni: {'pepperoni' in requested_topping}.")

#Testing conditions with if when multiple tests required
requested_topping = ['mushrooms', 'onions', 'pineapple']

if 'anchovies' in requested_topping:
    print("Adding anchovies.")
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'onions' in requested_topping:
    print("Adding onions.")
if 'pineapple' in requested_topping:
    print("Adding pineapple.")

print(f"\nFinished making your pizza!")

#Test for items not in the list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding topping {requested_topping}.")

print(f"\nFinished making your pizza!\n\nWith if-else statement:")

# Use a if-else to tell the customer you are out of a topping.
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers.")
    else:
        print(f"Adding topping {requested_topping}.")

print(f"\nFinished making your pizza!")

#Now what if the pizza has no toppings.
requested_toppings = []

# list returns True if not empty, False if empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding topping {requested_topping}.")
    print(f"\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Working with two lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding topping {requested_topping}.")
    else:
        print(f"Sorry we are out of {requested_topping}.")

print(f"\nFinished making your pizza!")