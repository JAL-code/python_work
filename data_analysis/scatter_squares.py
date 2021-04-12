import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
# smaller size for more values and set point color
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) 

# Set chart title and label axis.
ax.set_title("Long List of Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot_green.png', bbox_inches='tight')
