# Python Crash Course: Chapter 5, Eric Matthews, User Input and While Loops

# Count all odd numbers up to a set number.
# The loop only prints when the number is odd.
# If even it conitunes the count.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Leaving out an increment will run the loop forever. 
# This error will not be added to this exam.
x = 1
while x <= 5:
    print(x)
    x += 1 # <-- delete to test infinite loop.
# Warning!!! Deleted increment may crash terminal/program or worse!
# Press Cntl+C or close terminal to exit loop.  
# May loose work as well so save your work on all open programs before tests.
