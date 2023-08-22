#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import requests
import csv
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

        # Export data to CSV
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in tasks_done:
                csv_writer.writerow(
                    [user_id, name, task['completed'], task['title']])

        # Perform the check for correct number of tasks in CSV
        num_lines = 0
        with open(csv_filename, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                if line:
                    num_lines += 1

        if num_tasks_done == num_lines - 1:  # Subtract 1 to account for the header line
            print("Number of tasks in CSV: OK")
        else:
            print("Number of tasks in CSV: Incorrect")
    else:
        print(f"Error: {response.status_code}")
