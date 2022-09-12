#!/usr/bin/python3
"""
    extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    task = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(id))

    userName = user.json()['username']
    userId = user.json()['id']
    jsonTask = task.json()

    fileCsv = open('{}.csv'.format(userId), 'w')
    writer = csv.writer(fileCsv, delimiter=",", quotechar='"',
                        quoting=csv.QUOTE_ALL)
    for idx in jsonTask:
        writer.writerow([userId, userName, idx['completed'], idx['title']])
    fileCsv.close()
