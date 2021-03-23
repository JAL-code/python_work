# Python Crash Course: Chapter 5, Eric Matthews, if Statements
# Window 10

age = 18
# Test if numerical value is 18
print(age == 18)

# inequality check
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# mathematical comparisons
age = 19
print(f"Age < 21: {age < 21}")
print(f"Age <= 21: {age <= 21}")
print(f"Age > 21: {age > 21}")
print(f"Age >= 21: {age >= 21}")
print(f"Age was {age}.")


# Check multiple conditions with and
age_0 = 22
age_1 = 18
print(f"Are both A1, {age_0}, and A2, {age_1}, greater than or equal to 21?")
print(f"{age_0 >=21 and age_1 >=21}.")

age_1 = 22
print(f"Aging A2, {age_1}: {age_0 >=21 and age_1 >=21}.")

# Check multiple conditions with or
age_0 = 22
age_1 = 18
print(f"Are either A1, {age_0}, or A2, {age_1}, greater than or equal to 21?")
print(f"{age_0 >=21 or age_1 >=21}.")

age_0 = 18
print(f"Benjamin Button action for 4 years on A2, {age_0}: {age_0 >=21 or age_1 >=21}.")