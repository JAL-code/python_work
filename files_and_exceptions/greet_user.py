# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
import json

filename = 'username.json'
with open(filename) as f: # read only access
    username = json.load(f)
    print(f"Welcome back, {username}!")
