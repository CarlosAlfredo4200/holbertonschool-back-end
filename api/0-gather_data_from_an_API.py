#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    API_URL = 'https://jsonplaceholder.typicode.com'

    response = requests.get(
        f'{API_URL}/users/{employee_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        name = data[0]['user']['name']
        tasks_done = [task for task in data if task['completed']]
        num_tasks_done = len(tasks_done)
        num_tasks_total = len(data)

        print((
            f"Employee {name} is done with tasks "
            f"({num_tasks_done}/{num_tasks_total}):"
        ))

        for task in tasks_done:
            print(f"\t{task['title']}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    get_employee_todo_progress(employee_id)
