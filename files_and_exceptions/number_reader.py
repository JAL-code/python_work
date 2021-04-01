# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
import json

filename = 'numbers.json'
with open(filename) as f: # read only access
    numbers = json.load(f)

print(numbers)
