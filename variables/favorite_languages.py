#Python Crash Course, Eric Matthes, Chapter 2,
#Controlling whitespace

#Add a tab \t
print("Working with tabs")
print("Python")
print("\tVersion 3.9")
print("\n")
#Add a newline \n
print("Working with newlines")
print("Languages:\nPython\nC\nJavaScript")
print("\n")
#Add an outline by stacking Whitespace combination

print("Languages:\n\tPython\n\tTypescript\n\tJavaScript")
print("\n")

#Stripping spaces right space
favorite_language = 'python '
print(f"{favorite_language}<-- Space")
print("Strip right space")
print(f"{favorite_language.rstrip()}<-- No Space")

#Permanently stripped
favorite_language = favorite_language.rstrip()
print(f"{favorite_language.rstrip()}<-- Space removed")

#Stripping spaces left space
favorite_language = ' python'
print(f"Space -->{favorite_language}")
print("Strip left space")
print(f"No Space -->{favorite_language.lstrip()}")
print(f"Left space not removed -->{favorite_language.rstrip()}")
