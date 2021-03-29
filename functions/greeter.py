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

# Using a function in a while loop.  Add method to escape the code.
# In this code we add an if block that breaks on a True condition.

def get_formatted_name_fml(first_name, middle_name, last_name):
    """Return a full name (first, middle and last), neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your first name: ")
    print("(enter 'q' to quit at anytime)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    m_name = input("Middle name: ")
    if m_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name_fml(f_name, m_name, l_name)
    print(f"\nHello, {formatted_name}!")
