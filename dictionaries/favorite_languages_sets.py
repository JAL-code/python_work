# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# Sets remove all duplicates
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# loop through a list of values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# manual method to build a set
languages = { 'python', 'c', 'ruby', 'python'}
print(languages)

# remember if you see brackets without key: then its probably a set.