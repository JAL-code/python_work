# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

# 'w' write - erase contents before write
# 'r' read, 'a' append, 'r+' read and write
filename = "programming.txt"
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

filename = "programming_no_newline.txt"
# without newline the next write is added after the last character.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

filename = "programming_with_newline.txt"
# with newline the next write is on a new line
#works with spaces, tabs, blank line
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("\n")
    file_object.write("\tAsteriods\n")
    file_object.write("\tDefender\n")

with open(filename, 'a') as file_object:
    file_object.write("I love working with large datasets.\n")
    file_object.write("Also, I love creating apps that can run in a browser.\n")
