#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos_data = todos_response.json()

    json_filename = "{}.json".format(user_id)
    with open(json_filename, "w") as jsonfile:
        json.dump({
            user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos_data]
        }, jsonfile, indent=4)

    print("Data exported to {}".format(json_filename))
