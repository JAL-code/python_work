#sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"Default: {cars}.")

#in reverse
cars.sort(reverse=True)
print(f"Reverse: {cars}")

cars.sort(reverse=False)
print(f"Reverse False: {cars}")
temp_car = cars.pop(2)
cars.append(temp_car)
print(cars)
temp_car = cars.pop(1)
cars.insert(0, temp_car)
print(f"Reverted to original order: {cars}.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Default 2: {cars}.")

#Temporarily sorting the list
print(f"Original list: {cars}")

print("\nHere is the sorted list:")
print(sorted(cars))

print(f"But the order was not permanently changed: \n{cars}")

#Reverse the order, independent of alphabetical order.
cars.reverse()
print(cars)

#Get the length
print(len(cars))