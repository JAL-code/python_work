# Python Crash Course: Chapter 5, Eric Matthews, User Input and while loops

# remove the single instance from a list.
# while - remove example.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print("Cats in the house!\n")


while 'cat' in pets:
    pets.remove('cat')

print(pets)
print("See, the cats have left the area.")