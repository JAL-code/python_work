#avoid errors - access last item with -1
#Create a list
motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(f"Last Item: {motorcycles[-1]}")

#Produces IndexError with empty lists
motorcycles = []
print(motorcycles[-1])