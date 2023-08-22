#!/usr/bin/python3
"""Module documentation"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = requests.get(
        f'{API_URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        username = data[0]['user']['username']

        csv_filename = f"{user_id}.csv"
        with open(csv_filename, "w", encoding='utf-8', newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in data:
                writer.writerow(
                    [user_id, username, task['completed'], task['title']])

        print(f"Data exported to {csv_filename}")
    else:
        print(f"Error: {response.status_code}")
