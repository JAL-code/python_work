# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# Style alternate for a dictionary.  This is a dictionary of similar objects.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# looping through all dictionary key-pair
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# keys only
for name in favorite_languages.keys():
    print(name.title())

# same as . . .
for name in favorite_languages:
    print(name.title())

# match keys in other lists for a code block
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# find if a person was in the poll. The keys method returns a list of keys.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# loop through a list of keys in a sorted order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# loop through a list of values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())