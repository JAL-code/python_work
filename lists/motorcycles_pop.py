#Create a list
motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Pop the last item
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"Popped items: {popped_motorcycle}.")

#now use the popped item in a sentence
print(f"I never owned a {popped_motorcycle.title()}.")

#unpop the item
motorcycles.append(popped_motorcycle)
print(f"Unpop it {motorcycles}.")

#select the pop position with () at the end.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

