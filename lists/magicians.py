# For every magician in the list of magicians, print the magicians name.
# Singular name for action being done on each item.
# Plural names for the list.
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician)

# Do more complex actions.
for magician in magicians
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Summarize the operation
print(f"Thank you, everyone. That was a great show!")

#Forgot to indent next line after 'for' statement. -> IndentationError: expected an indented blook
#Indent line that does not require indentation.  -> IndentationError:  unexpected indent
#Forgot to indent additional lines after first for indented line -> Logical Error.
#(code may run, but result does not match intended action.)
#Forget the colon at the end of the the for statement.  -> Syntax Error: invalid syntax.