import requests
import json
import time

from plotly.graph_objs import Bar
from plotly import offline

# True: show test data for state of program.
test_code = False
# True: Load and save another API request from GitHub.
# False: Reload the last API request.
reload_saved_data = True
readable_file = 'data/readable_python_results.json'
# True, print out the data to the terminal
show_data = False

# Monitor your API requests to GitHub with this file.
# Goto the following page and update to find limit per hour
# https://api.github.com/rate_limit
# See resources -> search

if reload_saved_data:
    url = 'https://api.github.com/search/repositories?q=language:python&sort:updated-desc&topic:dynamo'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    # If 200, the API sent data and the data was recieved.
    print(f"Status code: {r.status_code}")

    # Store API response in a variable.
    response_dict = r.json()

    # Check time loaded
    limit_time = 1618250773
    localtime = time.asctime( time.localtime(limit_time))
    print ("Limit 10 current time :", localtime)
    timerun = time.asctime( time.localtime(time.time()) )
    print ("Runtime :", timerun)

if not reload_saved_data:
    # Explore the structure of the data.
    with open(readable_file) as f:
        response_dict = json.load(f)

print(f"Total respositories: {response_dict['total_count']}")

# Print out the keys for the data recieved/reloaded.
if test_code:
    # Process results.
    print(response_dict.keys())

readable_file = 'data/readable_python_results.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Example the first repository.
repo_dict = repo_dicts[0]
if test_code:
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)
        
# Process results
repo_names, stars = [], []

if show_data:
    print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    if show_data:
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Description: {repo_dict['description']}")

    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make visualization.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')





