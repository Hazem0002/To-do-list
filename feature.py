def mark_task_complete(index):
    if 0 <= index < len(tasks):
        completed_task = tasks.pop(index)
        print(f"Task completed: {completed_task}")
    else:
        print("Invalid task number.")