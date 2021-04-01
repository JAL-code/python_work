# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

# This code generates a ZeroDivisionError
# print(5/0)
# Use try-except Blocks to handle the exception.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero.")
