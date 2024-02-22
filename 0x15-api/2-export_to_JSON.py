#!/usr/bin/python3
"""
This script fetches user data and their todos from the JSONPlaceholder API
and exports the data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = f"{jsonplaceholder}/{USER_ID}"
    response = requests.get(url)
    username = response.json().get('username')
    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    data = {USER_ID: []}
    for task in tasks:
        data[USER_ID].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    with open(f"{USER_ID}.json", 'w') as f:
        json.dump(data, f)

