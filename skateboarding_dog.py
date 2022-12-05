# import tweepy
# import openai
import requests
import json

#its bad practice to place your bearer token directly into the script (this is just done for illustration purposes)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGxAkAEAAAAAKGurOt7foGHWQ6BZMDGZ8UY9yhw%3D0SSYHICsCfDna2asj9LRdVW7f8ErDibEYZTdWeoNDWUMB7QqiD"

# define search twitter function
def search_twitter(query, tweet_fields, bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    response = requests.request("GET", url, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#search term
query = "skateboarding dog"
#twitter fields to be returned by api call
tweet_fields = "tweet.fields=text,author_id,created_at"

#twitter api call
json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)
#pretty printing
print(json.dumps(json_response, indent=4, sort_keys=True))
