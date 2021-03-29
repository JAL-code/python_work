# Python Crash Course: Chapter 8, Eric Matthews, Functions

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user.
    **variable will create an empty dictionary and pack the key-values pairs inside.
    Like default values, arbitrary arguments are listed after Positional parameters.
    non_specific keyword arguments: **kwargs"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)