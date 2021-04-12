import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Print the header row
    # print(header_row)
    # print the header row to find row of interest.
    # for index, column_header in enumerate(header_row):
    #    print(f"{index}, {column_header}")
    # Get high temperatures, column 5, from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# print(highs) # print to output.

plt.style.use('seaborn')
fig, ax = plt.subplots() #figsize=(10, 6), dpi=128
# smaller size for more values and set point color
ax.plot(highs, c='red') 

# Set chart title and label axis.
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=16)

# Set the range for each axis.
# ax.axis([0, 1100, 0, 1100000])

# plt.savefig('squares_plot_green.png', bbox_inches='tight')
plt.show()
