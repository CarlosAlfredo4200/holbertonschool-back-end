#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = \
        requests.get(
            f'{API_URL}/users/{user_id}/todos',
            params={'_expand': 'user'}
        )

    if response.status_code == 200:
        data = response.json()
        name = data[0]['user']['name']
        tasks_done = [task for task in data if task['completed']]
        num_tasks_done = len(tasks_done)
        num_tasks_total = len(data)

        first_str = f"Employee {name} is done with tasks"

        print(f"{first_str}({num_tasks_done}/{num_tasks_total}):")
        for task in tasks_done:
            print(f"\t {task['title']}")
    else:
        print(f"Error: {response.status_code}")
