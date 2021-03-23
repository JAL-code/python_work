# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# KeyErrors are generated when the key is not in the dictionary.
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) -> KeyError: 'points'

#instead use get to pass alternate argument if key not found
point_value = alien_0.get('points', 'No point value assigned.') 
print(point_value)
