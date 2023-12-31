# Function to add a new task to the list
def add_new_task(tasks, task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added to the list!")


def completed_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        print(f"Task '{tasks[task_index - 1]['name']}' marked as completed!")
    else:
        print("Invalid task index!")

# Function to display the current to-do list


def display_task_all(tasks):
    if not tasks:
        print("To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{index}. [{status}] {task['name']}")


# Main function to run the to-do list app
def main():
    tasks = []
    print("Welcome to the To-Do List")

    while True:
        print("\nWhat do you want to do?")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed( please view tasks before)")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            display_task_all(tasks)
        elif choice == "2":
            task_name = input("Enter the task name: ")
            add_new_task(tasks, task_name)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            completed_task(tasks, task_index)
        elif choice == "4":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
