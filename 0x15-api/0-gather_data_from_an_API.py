#!/usr/bin/python3
"""
    using this REST API, for a given employee ID, returns information about
    his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    task = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(id))

    employeeName = user.json()['name']
    jsonTask = task.json()

    listTodo = []
    numberOfDoneTasks = 0
    totalNumberOfTasks = 0

    for idx in jsonTask:
        if idx['completed'] is True:
            listTodo.append(idx['title'])
            numberOfDoneTasks += 1
        totalNumberOfTasks += 1

    print("Employee {} is done with tasks({}/{}):".format(employeeName,
                                                          numberOfDoneTasks,
                                                          totalNumberOfTasks))

    for Todo in listTodo:
        print("\t {}".format(Todo))
