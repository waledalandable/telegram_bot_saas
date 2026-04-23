tasks = []

def add_task(task):
    tasks.append(task)

def get_task():
    if tasks:
        return tasks.pop(0)
