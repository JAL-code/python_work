import csv

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

print(highs)
