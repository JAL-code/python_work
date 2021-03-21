#Python Crash Course, Eric Matthes, Chapter 2, 
#Controling apostrophes, difference between single and double quotes.
#no error
message = "One of Python's strengths is its diverse community."
print(message)
#error - SyntaxError: invalid syntax" Note the highlighting ends at the ' on Python's.
message = 'One of Python's strengths is its diverse community.'
print(message)
