# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

# Example dictionary. Key = 'color','points'. Value = 'green', 5
# Key-value pair. 2 total markup by the comma.
alien_0 = {'color': 'green', 'points': 5}
# Get the value of a Key
print(alien_0['color'])
print(alien_0['points'])
# get the value from a key
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Dynamic structures, add as many key-pairs at any time.
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# What if we need an empty dictionary.  Use empty braces.
alien_0 = {}
# With keys in brackets assign the value
alien_0['color'] = 'green'
alien_0['points'] = 5
print(f"The alien is {alien_0['color']}.")
print(alien_0)
# Using the same assignment code reassign a new value.
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
#Track the alien!

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Make the alien fast.  Assign 'fast' as 'speed'.
alien_0['speed'] = 'fast'
#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Delete a key-pair
alien_0['points'] = 0
print(alien_0)

del alien_0['points']
print(alien_0)
