#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_dict={}):
    """ count_words` populates `word_dict` with count of words
    """
    try:
        if len(word_dict) != 0 and after is None:
            return None
        base_url = (
            "https://www.reddit.com/r/{}/hot.json{}"
            .format(
                subreddit,
                "?after="+after if after is not None else ""
            )
        )

        res = requests.get(
            base_url,
            headers={"User-agent": "PostmanRuntime/7.28.4"},
            allow_redirects=False
        )
        for child in res.json().get("data").get("children"):
            search_list(
                word_list,
                word_dict,
                child.get("data").get("title")
            )

        after = res.json().get("data").get("after")
        count_words(subreddit, word_dict, after, word_dict)
        if len(word_dict) != 0:
            for k, v in word_dict.items():
                print("{}: {}".format(k, v))
            word_dict.clear()
    except Exception as e:
        return None


def search_list(word_list, word_dict, title):
    """Search `title` for words in `word_list` and populate `word_dict'
    """
    for word in title.split():
        if word.lower() in " ".join(word_list).lower().split():
            if word_dict.get(word.lower()):
                word_dict[word.lower()] += 1
            else:
                word_dict[word.lower()] = 1
