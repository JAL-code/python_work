import csv
from datetime import datetime
# %A - Weekday, %B Month, %m Month 2 digit, %d Day number
# %Y - Year, 4dgt, %y 4 digit,
# %H 24Hr, %I 12hr, %p AM/PM, %M Minutes, %S Seconds

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Print the header row
    # print(header_row)
    # print the header row to find row of interest.
    # for index, column_header in enumerate(header_row):
    #    print(f"{index}, {column_header}")
    # Get high temperatures, column 5, from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
# print(highs, lows) # print to output.
plt.style.use('seaborn')
fig, ax = plt.subplots() #figsize=(10, 6), dpi=128

# smaller size for more values and set point color
ax.plot(dates, highs, c='red', alpha=0.5) 
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set chart title and label axis.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=16)

# Set the range for each axis.
# ax.axis([0, 1100, 0, 1100000])

# plt.savefig('squares_plot_green.png', bbox_inches='tight')
plt.show()
