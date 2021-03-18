#Python Crash Course, Eric Matthes, Chapter 3,
#Lists

#prints out the representation of the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  #first bicyle in the list  is trek.
print(bicycles[0].title()) #as a noun

#getting other items
print(bicycles[1].title()) #2nd item
print(bicycles[3].title()) #4th item

#print the last element in the row with the end position to it's right
print(bicycles[-1].title())

#Reference the list items in a string.
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)