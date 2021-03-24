# Python Crash Course: Chapter 5, Eric Matthews, User Input and While Loops
# Windows 10

# Clear, easy to use prompt for information request
# Add a colon, question mark, or exclaimation point with a space

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Options: use a string variable for the information request
# If request is longer than the 79 limit, Add the end string at the next line
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# What if the data is numerical?
age = input("How old are you? ")
print(age)
# age > 13
# In the python3 terminal prints 'age' as string. 
# Conditionally, this comparision  gives a ->
# TypeError: unorderable types: str() >= int()
# So convert the string into the data type preferred.
age = int(age)
print(F"18 or older? {age >= 18}")

