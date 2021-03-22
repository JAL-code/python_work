# Python Crash Course: Chapter 4, Eric Matthews, Working with Lists
# Using range() function generate a series of numbers.
# Generates a one off series of numbers from 1 to 4.
for value in range(1,5):
    print(value)

# To get five goto 6
for value in range(1,6):
    print(value)

# Another way, just use range(6)
for value in range(6):
    print(value)

# create a list of numbers with range
numbers = list(range(1,6))
print(numbers)

# or create a list of even numbers with range
even_numbers = list(range(2,11,2))  
# Start at 2, go to 11, add 2 for next value
print(even_numbers)
