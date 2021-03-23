# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Windows 10

# if-elif-else chain
# the else statement is the catchall statement.
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Or just select the price and then print the statement.
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# Add as many elif blocks as you want
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# Add as many elif blocks as you want and leave out the else.
# Conditional requires every code to pass a specific text.
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
