#  Source code - https://github.com/HackerNews/API
from operator import itemgetter

import requests

show_data = True
save_to_dict = True
sort_dict = True
print_dict = True

# Make an API call and store the response.
# Root URL for site
main_url = 'https://hacker-news.firebaseio.com/v0/'
# sub-URL with list of top stories
start_location = 'topstories.json'
test_url = f'{main_url}{start_location}'
r = requests.get(test_url)
print(f"Status code: {r.status_code}")

# Process the information about each submission.
submission_ids = r.json()
# store submission ids in a list
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"{main_url}item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\t\tstatus: {r.status_code}")
    response_dict = r.json()

    if show_data:
        print(response_dict)

    if save_to_dict:
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        # descendants -> number of comments received.
        # kids -> IDS of all comments made (usually less than descendants
        # title ->
        # hn_link -> URL for the article.
        submission_dicts.append(submission_dict)

if sort_dict:
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                                reverse=True)

if print_dict:
    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")