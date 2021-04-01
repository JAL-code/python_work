# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f: # read only access
    json.dump(username, f)
    print(f"We'll remember you when you come back online, {username}!")
