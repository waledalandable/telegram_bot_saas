from queue_system import get_task
from transfer import run_transfer
import time

def start_worker(bot):
    while True:
        task = get_task()
        if task:
            run_transfer(task["source"], task["target"], bot, task["chat_id"])
        time.sleep(3)
