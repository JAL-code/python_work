# Python Crash Course: Chapter 8, Eric Matthews, Functions

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

def build_person_add(first_name, last_name, age=None):
    """Return a dictionary of information about a person.
    Adding the age is optional.
    first_name, last_name, age
    None evaluates to false.  So if age is an argument,
    then the age will be added to the dictionary."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

actor = build_person('james', 'dean')
print(actor)

actor = build_person_add('james', 'dean', age='27')
print(actor)