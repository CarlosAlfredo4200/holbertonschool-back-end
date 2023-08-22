#!/usr/bin/python3
"""
Import the module requests
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    print((
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    ))
    print(f"{employee_name}: name of the employee")
    print(f"{len(done_tasks)}: number of completed tasks")
    print(f"{total_tasks}: total number of tasks")

    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)
