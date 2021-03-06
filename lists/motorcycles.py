#Create a list
motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Modify element 0
motorcycles[0] = 'moto guzzi'
print(motorcycles)

#Append an element
motorcycles.append('ducati')
print(motorcycles)

#Start all over again. Redefine a new list.
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f"Back to the beginning: {motorcycles}.")

#Insert another element in the list.
motorcycles.insert(1, 'ducati')
print(f"Inserted a new motorcycle at position 2 {motorcycles}.")

#del an element
del motorcycles[0]
print(f"Delete first item: {motorcycles}.")

del motorcycles[1]
print(f"Cut out the middle man: {motorcycles}.")

#Create another list
motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#Remove the item without knowing the position
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
