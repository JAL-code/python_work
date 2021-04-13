import requests
import json
import time

test_code = False
reload_saved_data = False
readable_file = 'data/readable_python_results.json'

# Monitor your API requests to GitHub with this file.
# Goto the following page and update to find limit per hour
# https://api.github.com/rate_limit
# See resources -> search

if reload_saved_data:
    url = 'https://api.github.com/search/repositories?q=language:python&sort:updated-desc&topic:dynamo'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
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

print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")





