# Python Crash Course: Chapter 8, Eric Matthews, Functions

# printing_models.py without functions.
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all the models that were printed.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
# This code is harder to modify.