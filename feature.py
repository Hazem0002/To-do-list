




















def delete_task(index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task deleted: {deleted_task}")
    else:
        print("Invalid task number.")