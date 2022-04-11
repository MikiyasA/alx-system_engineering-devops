#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
url: https://jsonplaceholder.typicode.com/
"""
import sys
import requests
import csv


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
        lct.append([usrid,
                    name,
                    task.get('completed'),
                    task.get('title')])

    fname = '{}.csv'.format(usrid)

    with open(fname, 'w') as emply_f:
        emply_w = csv.writer(emply_f,
                             delimiter=',',
                             quotechar='"',
                             quoting=csv.QUOTE_ALL)

        for task in lct:
            emply_w.writerow(task)
