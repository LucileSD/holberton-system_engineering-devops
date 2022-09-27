#!/usr/bin/python3
"""
    requests module
"""
import requests


def top_ten(subreddit):
    """
        queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit
    """
    response = requests.get("https://www.reddit.com/r/" + subreddit +
                            "/hot.json",
                            headers={'User-agent': 'your bot 0.1'})
    if response.status_code == 404:
        print("None")
    else:
        search = response.json()['data']['children']
        for title in search[:10]:
            print(title['data']['title'])
