#!/usr/bin/python3
"""
    export data in the JSON format for all the users
"""
import json
import requests

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')

    jsonUser = user.json()

    userDict = {}

    for user in jsonUser:
        userID = user['id']
        task = requests.get(
                       'https://jsonplaceholder.typicode.com/users/{}/todos'
                       .format(userID))

        jsonTask = task.json()

        userDict[str(user['id'])] = []

        for idx in jsonTask:
            userDict[str(user['id'])].append({"username": user['username'],
                                              "task": idx['title'],
                                              "completed": idx['completed']})

    file = open("todo_all_employees.json", 'w')
    json.dump(userDict, file)
    file.close()
