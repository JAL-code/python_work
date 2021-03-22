# Python Crash Course: Chapter 4, Eric Matthews, Working with lists
my_foods = ['steel cut oats', 'chicken bbq pizza', 'raspberry chocolate icecream']
#copy the list
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('meatloaf')
friend_foods.append('salad')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#Assign the variables to the same list.  Why you copy as a slice.
friend_foods = my_foods

my_foods.append('meatloaf')
friend_foods.append('salad')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)