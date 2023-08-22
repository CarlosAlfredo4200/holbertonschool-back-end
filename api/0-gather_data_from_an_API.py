#!/usr/bin/python3
import requests
import sys

"""
Module documentation containig a lot of lines
"""


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Obtener detalles del empleado
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    # Obtener la lista de tareas del empleado
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    # Imprimir el progreso de las tareas del empleado
    print(
        f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    print(f"{employee_name}: name of the employee")
    print(f"{len(done_tasks)}: number of completed tasks")
    print(f"{total_tasks}: total number of tasks")

    for task in done_tasks:
        print(f"\t{task['title']}")


# Verificar si el script se está ejecutando como programa principal
if __name__ == "__main__":
    # Verificar si se proporcionó un argumento (ID del empleado)
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Convertir el argumento en un número entero (ID del empleado)
    employee_id = int(sys.argv[1])

    # Llamar a la función para obtener y mostrar el progreso de tareas del empleado
    get_employee_todo_progress(employee_id)
