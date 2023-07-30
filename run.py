# to do list 
# Function to add a new task to the list
def add_task(tasks, task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added to the list!")