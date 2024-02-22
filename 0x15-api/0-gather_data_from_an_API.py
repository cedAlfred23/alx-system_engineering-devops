#!/usr/bin/python3
"""Generate a Todo list for a given employee id"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)
    
    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(base_url + f"users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: User not found")
        exit(1)
    user = user_response.json()
    employee_name = user.get('name')  # Adjusted to fetch the correct field

    # Fetch todos
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Todos not found")
        exit(1)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    
    # Output progress
    total_tasks = len(todos)
    completed_task_count = len(completed_tasks)
    print(f"Employee {employee_name} is done with tasks ({completed_task_count}/{total_tasks}):")
    print(f"{employee_name}")
    print(completed_task_count)
    print(total_tasks)
    for task in completed_tasks:
        print(f"\t{task}")


