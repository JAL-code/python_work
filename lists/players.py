# Python Crash Course: Chapter 4, Eric Matthews, Working with lists
# slice = a specific group in a list - index 0 to index 3
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])
# Add the forth
print(players[0:4])
# Same result, just starts at the beginning
print(players[:4])
# Remove index 0
print(players[1:4])
#  From 3rd item to the last index - unspecified.
print(players[2:]) #subtract 1 from desired index.
# Same result but from last item to -3
# [  ,  ,  ,  ,  ,  ]
# 0  1  2  3  4  5  6
# -6 -5 -4 -3 -2 -1 0
print(players[-3:])