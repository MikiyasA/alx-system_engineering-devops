#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
url: https://jsonplaceholder.typicode.com/
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    usr = '{}users/{}'.format(url, sys.argv[1])
    r = requests.get(usr)
    j = r.json()

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    r = requests.get(todos)
    tasks = r.json()
    lct = []
    for task in tasks:
        if task.get('completed') is True:
            lct.append(task)

    print("Employee {} is done with tassks({}/{}):".format(
        j.get('name'), len(lct), len(tasks)))
    for task in lct:
        print("\t {}".format(task.get('title')))
