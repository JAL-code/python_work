# Python Crash Course: Chapter 8, Eric Matthews, Functions

def get_formatted_name_fl(first_name, last_name):
    """Return a first and last name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_formatted_name_fml(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted.
    First name and last name are default order with middle name optional.
    Create an optional assignment with "parameter=''". """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_fl('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_fml('jimi', 'jack', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)