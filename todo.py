import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    tasks = []
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split("|", 1)
            if len(parts) == 2:
                tasks.append(parts)
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for status, desc in tasks:
            file.write(f"{status}|{desc}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\nTo-Do List:")
        for idx, (status, desc) in enumerate(tasks, start=1):
            box = "[x]" if status == "1" else "[ ]"
            print(f"{idx}. {box} {desc}")
    print()

def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(["0", task])  
        save_tasks(tasks)
        print("Task added.\n")
    else:
        print("Task description cannot be empty.\n")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed[1]}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def edit_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to edit: "))
        if 1 <= index <= len(tasks):
            new_task = input("Enter the new task description: ").strip()
            if new_task:
                tasks[index - 1][1] = new_task
                save_tasks(tasks)
                print("Task updated.\n")
            else:
                print("New task description cannot be empty.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def toggle_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to toggle complete/incomplete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1][0] = "1" if tasks[index - 1][0] == "0" else "0"
            save_tasks(tasks)
            print("Task status updated.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Mark/Unmark Task as Done")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            toggle_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.\n")

if __name__ == "__main__":
    main()
