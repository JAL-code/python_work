# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions

# FileNotFoundError example
filename = 'alice.txt'

# comment this section to test working solution.
# with open(filename, encoding='utf-8') as f:
#    contents = f.read()
# delete from here down to get error.

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
# Move file into same location to split the file text.
else:
    # Count the number of words in the title.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} contains {num_words}.")
