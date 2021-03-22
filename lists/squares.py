#Python Crash Course: Chapter 4, Eric Matthews, Working with lists
#Another sequence generating a list.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(f"Temporary value: {squares}.")

#Refactored to append new value directly to the list
squares= []
for value in range(1, 11):
    squares.append(value ** 2)

print(f"Direct append: {squares}.")

# Check some of the basic statistical functions with python.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Digits: {digits}.")
print(f"Min: {min(digits)}, Max: {max(digits)}, Sum: {sum(digits)}.")
