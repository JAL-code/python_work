# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

from access import get_location_for_code
# create a module called access.py that gives the location for the file_reader to get this macro to run.  Call the function: get_location_for_code()

file_path = get_location_for_code()
file_name = 'pi_digits.txt'
with open(f"{file_path}{file_name}") as file_object:
    contents = file_object.read()
# this code relies on python to close() the file.  Hence close is not used in this example.

# print whitespace (blank line)
print(contents)

# remove whitespace
print(contents.rstrip())