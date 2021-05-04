import os
import requests
import json
import sys

from ignore_location import set_home
# create a file with the root location of this file and return
# the location through a function called set_home.
# the python script is saved as ignore_location for github to ignore.

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

print(set_home())
os.chdir(set_home())

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()

# Print the data
print(response_dict.keys())
print(response_dict.values())

readable_file = './data/readable_hn_data.json'
with open(readable_file, 'w') as file:
    json.dump(response_dict, file, indent=4)