# Test the url prior to running the script.

# Make an API call and store the response.
main_url = 'https://hacker-news.firebaseio.com/v0/'
start_location = 'topstories.json'
test_url = f'{main_url}{start_location}'

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# https://hacker-news.firebaseio.com/v0/topstories.json

if test_url == url:
    print('Good')

submission_id = '00190923'

# Make a separate API call for each submission.
url_2 = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
print(url_2)

# Make a separate API call for each submission.
test_url_2 = f"{main_url}item/{submission_id}.json"
print(test_url_2)

if test_url_2 == url_2:
    print('Good')
else:
    print('Bad')