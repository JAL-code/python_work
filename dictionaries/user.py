# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# Style alternate for a dictionary.  This is a dictionary of similar objects.
user_0 = {
    'username': 'efermi',
    'alias_first': 'enrico',
    'alias_last': 'fermi',
    'first_name': 'John',
    'middle_name': 'Skittle',
    'last_name' : 'Longstockings',
    'nick_name': 'Skippy',
    'title': 'Mr.',
    'extra_name' : 'Jr.',
}

# create names for the key-value pair
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

