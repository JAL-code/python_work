# Python Crash Course: Chapter 5, Eric Matthews, User Input and while loops

# Type in 'quit' to end the program. While loop exits when active is False.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Was ==.  Prints quit.
# Is != To fix, change to not equal to avoid printing a message.
print("\nNew version:")
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Type in 'quit' to end the program. While loop exits when active is False.
prompt = "\nTell me something, and I will repeat it back to you(v2):"
prompt += "\nEnter 'quit' to end the program. "

active = True  # <-- This is a flag. It acts as a signal to the program
# Flags expand the capacity to test conditions in a program.
while active:
    message = input(prompt)


    if message == 'quit':
        active = False
    else:
        print(message)
