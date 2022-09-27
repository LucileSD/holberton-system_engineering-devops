#!/usr/bin/python3
"""
    file 0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
        querie the Reddit API and returns the number of subscribers for a given
        subreddit
    """
    response = requests.get("https://www.reddit.com/r/" + subreddit +
                            "/about.json",
                            headers={'User-agent': 'your bot 0.1'})
    if response.status_code == 404:
        return 0
    return response.json()["data"]["subscribers"]
