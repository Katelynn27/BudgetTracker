import JSON
file_name = 'ToDo.json'  #loction of to do list tasks

def loadTasks():
  try:
    with open(file_name, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    print("Error: File not found.")

def save_tasks(tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"Description": description, "Complete?": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def remove_task(task_index):
    tasks = load_tasks()
    try:
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['description']}")
    except IndexError:
        print(f"Error: Task {task_index} does not exist.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. [{status}] {task['description']}")

def mark_as_done(task_index):
    tasks = load_tasks()
    try:
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task as done: {tasks[task_index]['description']}")
    except IndexError:
        print(f"Error: Task {task_index} does not exist.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. View To-Do List")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '3':
            task_index = int(input("Enter task number to remove: "))
            remove_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to mark as done: "))
            mark_as_done(task_index)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
