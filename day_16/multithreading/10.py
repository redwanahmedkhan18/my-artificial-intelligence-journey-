from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n*n

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(task, range(10))

print(list(results))