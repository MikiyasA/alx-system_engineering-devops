#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
url: https://jsonplaceholder.typicode.com/
"""
import sys
import requests
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    usr = '{}users'.format(url)
    r = requests.get(usr)
    j = r.json()
    d_task = {}

    for usr in j:
        name = usr.get('username')
        usrid = usr.get('id')
        todos = '{}todos?userId={}'.format(url, usrid)
        r = requests.get(todos)
        tasks = r.json()
        lct = []
        for task in tasks:
            dic_task = {"username": name,
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            lct.append(dic_task)

        d_task[str(usrid)] = lct

    fname = 'todo_all+employees.json'
    with open(fname, 'w') as f:
        json.dump(d_task, f)
