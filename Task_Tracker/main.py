import json
import time
FILE_PATH = "tasks.json"

def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

tasks = load_tasks()

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def status_to_string(status):
    if status == 1:
        return "Done"
    elif status == 2:
        return "In Progress"
    elif status == 3:
        return "Not Done"
    else:
        return "Invalid status"

def menu():
    while True:
        print("\nPlease choose an option:")
        print("0. View Tasks")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Completed tasks")
        print("5. View tasks in progress")
        print("6. Exit")

        choice = input("Enter number here: ")

        if choice == '0':
            view_task()
        elif choice == '1':
            add_task()
        elif choice == '2':
            update_task()
        elif choice == '3':
            delete_task()
        elif choice == '6':
            print("Thank you for using the task manager")
            print("The system will now shutdown")
            break
        elif choice == '4':
            completed_task()
        elif choice == '5':
            tasks_in_progress()
        else:
            print("Please select a valid number from the given choices")

def view_task():
    if not tasks:
        print("Currently empty, please add tasks")
    else:
        for task in tasks:
            if task['status'] ==1:
                continue
            status_str = status_to_string(task['status'])
            print(f"ID: {task['id']} | Title: {task['title']} |Description: {task['description']} | Status: {status_str}| "f"CreatedAt: {format_time(task['createdAt'])} | "
                f"Updated At: {format_time(task['updatedAt'])} "
                )

def add_task():
    while True:
        title = input("Enter task title: ")
        if title:
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")
    while True:
        description = input("Enter task description")
        if description:
            break
        else:
            print("Description cannot be empty. Please enter a valid description.")

    while True:
        status = input("Enter task status (1 for Done, 2 for In Progress, 3 for Not Done): ")
        if status in ['1', '2', '3']:
            break
        else:
            print("Invalid status. Please enter 1 (Done), 2 (In Progress), or 3 (Not Done).")

    id = len(tasks) +1
    created_at = updated_at = time.time()
    tasks.append({
        'id': id,
        'title': title,
        'description': description,
        'status': 3,
        'createdAt': created_at,
        'updatedAt': updated_at
    })
    print(f"Task '{title} added successfully")
    save_tasks()

def update_task():
    task_id = int(input("Enter task ID to update: "))
    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return

    print(f"Updating task ID {task_id}...")
    new_title = input(f"Enter new title (current: {task['title']}): ") or task['title']
    new_description = input(f"Enter new description (current: {task['description']}): ") or task['description']
    new_status = input(f"Enter new status (1 for Done, 2 for In Progress, 3 for Not Done, current: {task['status']}): ")

    updated_at = time.time()
    new_status = int(new_status) if new_status else task['status']

    task['title'] = new_title
    task['description'] = new_description
    task['status'] = new_status
    task['updatedAt'] = updated_at

    print(f"Task ID {task_id} updated.")
    save_tasks()

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return

    tasks.remove(task)

    print(f"Task ID {task_id} deleted.")
    save_tasks()

def completed_task():
    if not tasks:
        print("please make a task")
        return

    print("\nCompleted Tasks (Status:Done): ")

    for task in tasks:
        if task['status'] ==1:
            print(f"ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | "
                  f"Status: {status_to_string(task['status'])} | Created At: {format_time(task['createdAt'])} | "
                  f"Updated At: {format_time(task['updatedAt'])}")

def tasks_in_progress():
    if not tasks:
        print("please make a task")
        return

    print("\nCompleted Tasks (Status:In Progress): ")
    for task in tasks:
        if task['status'] ==2:
            print(f"ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | "
                  f"Status: {status_to_string(task['status'])} | Created At: {format_time(task['createdAt'])} | "
                  f"Updated At: {format_time(task['updatedAt'])}")
menu()
