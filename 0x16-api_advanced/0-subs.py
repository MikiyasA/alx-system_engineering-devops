#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """ the methods returns the number of subscribers
    """
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=hdr, allow_redirects=False)

    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
