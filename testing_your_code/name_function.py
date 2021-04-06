# Python Crash Course: Chapter 11, Eric Matthews, Testing Your Code

def get_formatted_name(first, last, middle=''):
    '''Generate a neatly formatted full name.'''
    if middle:  # test if middle is not empty
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
