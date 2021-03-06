#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
url: https://jsonplaceholder.typicode.com/
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    usrid = sys.argv[1]
    usr = '{}users/{}'.format(url, usrid)
    r = requests.get(usr)
    j = r.json()
    name = j.get('username')

    todos = '{}todos?userId={}'.format(url, usrid)
    r = requests.get(todos)
    tasks = r.json()
    lct = []
    for task in tasks:
        dic_task = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": name}
        lct.append(dic_task)

    dt = {str(usrid): lct}
    filename = '{}.json'.format(usrid)
    with open(filename, 'w') as f:
        json.dump(dt, f)
