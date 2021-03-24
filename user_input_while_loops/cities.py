# Python Crash Course: Chapter 5, Eric Matthews, User Input and while loops

# Use break to exit a while loop.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# break can be used in other loops such as for, if.
