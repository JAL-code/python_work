#Python Crash Course, Eric Matthes, Chapter 2, 
#format function with strings up to Python 3.5

first_name = "ada"
last_name = "lovelace"
full_name = "{} {}".format(first_name, last_name)
message = "Hello, {}!".format(full_name.title())
print(message)

