# Python Crash Course: Chapter 4, Eric Matthews, Working with lists
# Working with tuples, a value that is immutable.
dimensions = (100, 50)
print(dimensions[0])
print(dimensions[1])
#try to reassign the first value
#dimensions[0] = 250
#generates a TypeError: 'tuple' object does not support item assignment
#for one assignment
my_t = (3,)
print(my_t)
#Looping tuples
for dimension in dimensions:
    print(dimension)

#instead of modifing the variable just reassign it with a new tuple.
dimensions = (250,0)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)