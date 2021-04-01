# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

from access import get_location_for_code
# create a module called access.py that gives the location
# for the file_reader to get this macro to run.
# Call the function: get_location_for_code()

file_path = get_location_for_code()

file_name = 'pi_digits.txt'
with open(f"{file_path}{file_name}") as file_object:
    # load the file into a list
    lines = file_object.readlines()
# this code relies on python to close() the file.
# Hence close is not used in this example.
# print the lines from the list.
for line in lines:
    print(line.rstrip())

# print the lines from the list joined.
pi_string = ''
pi_string2 = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(f"{len(pi_string)} characters.")

# print the lines from the list without the left spaces for indentation.

for line in lines:
    pi_string2 += line.strip()

print(pi_string2)
print(f"{len(pi_string2)} characters.")

# This value is a string. Convert to float for numerical operations.
print(type(pi_string2))
print(f"A 3 ft circle has a circumference of {2*float(pi_string2)*3} ft.")