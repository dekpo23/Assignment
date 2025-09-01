# Simple To-Do List Application

from pathlib import Path

# List to store tasks
tasks = []


# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")

# Function to Save tasks
def save_tasks():
    working_directory = Path.cwd()
    new_file = working_directory / 'todo_list.txt'
    if new_file.exists():    
        with open(new_file, 'a', newline = '', encoding = 'utf-8') as f:
            f.writelines(tasks)
    else:
        with open(new_file, 'w', newline = '', encoding = 'utf-8') as f:
            f.writelines(tasks)

def complete_tasks():
    print('/n'.join(tasks))
    task_status = {task: input(f'{task} status(Enter 1 if Completed, 2 if In Progress and 3 if Not Started): ') for task in tasks}
    completed_tasks_dic = dict(filter(lambda x: x[1] == '1', task_status.items()))
    return completed_tasks_dic

def urgent_tasks():
    print('/n'.join(tasks))
# Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Tasks  4. Exit")

    # Ask user for their choice
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting program. Have a productive day!")
        break
    else:
        print("Invalid choice! Please select a valid option.")