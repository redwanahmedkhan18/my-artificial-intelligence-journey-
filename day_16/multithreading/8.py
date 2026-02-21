from threading import Thread
from queue import Queue
import time
import random

class TaskProducer(Thread):
    def __init__(self, queue, total_tasks):
        super().__init__()
        self.queue = queue
        self.total_tasks = total_tasks

    def run(self):
        for i in range(self.total_tasks):
            task = f"task-{i}"
            print(f"[Producer] Created {task}")
            self.queue.put(task)
            time.sleep(random.uniform(0.3, 1))

        for _ in range(3):   # shutdown signals
            self.queue.put(None)


class Worker(Thread):
    def __init__(self, queue, wid):
        super().__init__()
        self.queue = queue
        self.wid = wid

    def run(self):
        while True:
            task = self.queue.get()
            if task is None:
                break

            print(f"[Worker-{self.wid}] Processing {task}")
            time.sleep(random.uniform(0.5, 1.5))
            self.queue.task_done()


class ThreadPool:
    def __init__(self, num_workers):
        self.queue = Queue()
        self.workers = [Worker(self.queue, i+1) for i in range(num_workers)]

    def start(self, total_tasks):
        producer = TaskProducer(self.queue, total_tasks)

        for w in self.workers:
            w.start()

        producer.start()

        producer.join()
        for w in self.workers:
            w.join()


if __name__ == "__main__":
    pool = ThreadPool(num_workers=3)
    pool.start(total_tasks=10)