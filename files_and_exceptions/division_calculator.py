# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

# This code generates a ZeroDivisionError
# print(5/0)
# Use try-except Blocks to handle the exception.
# Enter the error type and then the message for the error.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# code block that calculates division with error exception.
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nFirst number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by zero.")
    else:
        print(answer)
