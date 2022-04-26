#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ a mothod returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)

    hdr = {'User-Agent': 'Mozilla/5.0'}

    res = requests.get(url, headers=hdr, allow_redirects=False)

    if (res.status_code == 200):
        dic = res.json()
        data_list = dic['data']['children']
        for i in data_list:
            hot_list.append(i['data']['title'])
            after = dic['data']['after']
        if (after is not None):
            recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    else:
        return (None)
    return (hot_list)
