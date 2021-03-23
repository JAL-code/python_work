# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# A dictionary in a dictionary. Let's get complicated.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

# Access the username and value of name and location 
# saved in dictionary
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # create the name and location variables.
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")