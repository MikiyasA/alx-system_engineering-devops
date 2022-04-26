#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ the methods returns titles of the first 10 hot posts
    """
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=hdr, allow_redirects=False,
                       params={'limit': 10})

    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
