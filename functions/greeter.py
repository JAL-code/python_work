# Python Crash Course: Chapter 8, Eric Matthews, Functions

def greet_user():  # function definition with no information in parathesis and ending with colon.
    # the body of the function
    """Display a simple greeting"""  # <-- docstring for function.
    print("Hello!")  # <-- line of code for the body

def greet_user_1(username):  # username is a parameter
    """Display a simple greeting. username is the name of the person to be greeted"""
    """username is a string."""
    print(f"Hello, {username.title()}!")

greet_user()
greet_user_1('jesse')  # jesse is the example of an argument.