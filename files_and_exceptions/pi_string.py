# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

from access import get_location_for_code
# create a module called access.py that gives the location
# for the file_reader to get this macro to run.
# Call the function: get_location_for_code()

file_path = get_location_for_code()

file_name = 'pi_million_digits.txt'
with open(f"{file_path}{file_name}") as file_object:
    # load the file into a list
    lines = file_object.readlines()


    
# this code relies on python to close() the file.
# Hence close is not used in this example.
# print the lines from the list joined.
pi_string = ''
pi_string2 = ''
for line in lines:
    pi_string2 += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string2:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(f"{pi_string2[:52]}")
print(f"{len(pi_string2)} characters.")

# This value is a string. Convert to float for numerical operations.
print(type(pi_string2))
# The following line generates a ValueError because its too long.

print(f"A 3 ft circle has a circumference of {2*float(pi_string2)*3} ft.")
 
pi_string=[pi_string2[:value] for value in range(1, 53)]
circumference = [2*float(value)*3 for value in pi_string]

calculation_pairs = []

for pair in range(len(pi_string)):
    new_pair = {'number_digits': pair, 'radius': pi_string[pair], 'circumference': circumference[pair]}
    calculation_pairs.append(new_pair)

for pair in calculation_pairs:
    print(f"{pair['number_digits']} digits rounds pi to {pair['radius']} with a 3 foot circumference of {pair['circumference']:}.")
# Add :.xf to format the calc. value to x digit after decimal.

