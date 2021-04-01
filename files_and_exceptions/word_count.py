# Python Crash Course: Chapter 10, Eric Matthews, Files and Exceptions
# JAL-code: adding a toggle for testing is a personal preference.
# When false, this removes annoying messessages the user may not prefer.
silentmode = True

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        if silentmode:
            pass # Pass lets the error fail silently.
                 # Pass also acts as a placeholder for future changes.
        # Remove pass to allow printing the error.
        else:
            print(f"Sorry, the file {filename} does not exist.")
    # Move file into same location to split the file text.
    else:
    # Count the number of words in the title.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} contains {num_words}.")

# FileNotFoundError example
filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt',
             'siddharth.txt',
             'moby_dick.txt',
             'little_women.txt'
             ]
for filename in filenames:
    count_words(filename)
