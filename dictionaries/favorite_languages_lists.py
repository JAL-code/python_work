# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# Style alternate for a dictionary.  
# This is a dictionary of similar objects.
# The value of pair is a list.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# looping through through this type dictionary requires 
# a 2nd loop to get the values
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Any deeper nesting is contrary to the Zen of Python. 
# So, make it simple or be a fool!
