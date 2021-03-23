# Python Crash Course: Chapter 5, Eric Matthews, Dictionaries
# Windows 10

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Let's make a fleet
aliens = []

# Make 30 green aliens. Range is a series of numbers to give how times
# to create a new alien.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens created:
print(f"Total number of aliens created: {len(aliens)}")

# Make the first aliens faster.
for alien in aliens[:3]:
    alien['color'] = 'green'
    alien['points'] = 10
    alien['speed'] = 'medium'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens created:
print(f"Total number of aliens created: {len(aliens)}")

# Make the second group of aliens faster.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Make the second group of aliens faster.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")