#!/usr/bin/python3
"""
    requests module
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit
    """
    if after is None:
        return

    response = requests.get("https://www.reddit.com/r/" + subreddit +
                            "/hot.json",
                            headers={'User-agent': 'holbie'},
                            params={'after': after}
                            )
    if response.status_code != 200:
        return None

    search = response.json()['data']
    for title in search['children']:
        hot_list.append(title)
    recurse(subreddit, hot_list, search['after'])
    return hot_list
