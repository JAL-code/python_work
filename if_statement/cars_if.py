# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Window 10

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional Testing
car = 'bmw'
# True case
print(car == 'bmw')
# False case
car = 'audi'
print(car == 'bmw')
#Test for equality is case sensitive.
car = 'Audi'
print(car == 'audi')
# test the value in lowercase
print(car.lower() == 'audi')