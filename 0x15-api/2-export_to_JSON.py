#!/usr/bin/python3
"""
    export data in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    task = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(id))

    employeeName = user.json()['username']
    employeeId = user.json()['id']
    jsonTask = task.json()

    userDict = {employeeId: []}

    for idx in jsonTask:
        userDict[employeeId].append({"task": idx['title'],
                                     "completed": idx['completed'],
                                     "username": employeeName})

    file = open("{}.json".format(employeeId), 'w')
    json.dump(userDict, file)
    file.close()
