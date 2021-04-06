# Python Crash Course: Chapter 11, Eric Matthews, Testing Your Code

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    # User can enter a series of names.
    first = input("\nPlease give me a first name: ")
    # Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    # User can q at anytime while entering last name.
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, middle, last)
    print(f"\tNeatly formatted name: {formatted_name}.")