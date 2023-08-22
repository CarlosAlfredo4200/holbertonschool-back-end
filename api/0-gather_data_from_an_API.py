#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos_data = todos_response.json()

    completed = [t for t in todos_data if t.get("completed")]
    completed_titles = [t.get("title") for t in completed]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed), len(todos_data)))
    for title in completed_titles:
        print("\t {}".format(title))
