# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Windows 10

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

# Using keyword 'not' allows to check if an item is not in a list.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
