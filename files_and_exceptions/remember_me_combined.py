# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
# Refactored as a function.

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your username? ")
        with open(filename, 'w') as f: 
            json.dump(username, f)
            print(f"We'll remember you when you come back online, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()
