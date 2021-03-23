# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Window 10

#test for inequality or "not"
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#check if value is in a list?
requested_topping = ['mushrooms', 'onions', 'pineapple']
print(requested_topping)
print(f"Mushrooms{'mushrooms' in requested_topping}.")
print(f"Pepperoni: {'pepperoni' in requested_topping}.")
