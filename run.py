# to do list 
# Function to add a new task to the list
def add_task(tasks, task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added to the list!")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        print(f"Task '{tasks[task_index - 1]['name']}' marked as completed!")
    else:
        print("Invalid task index!")