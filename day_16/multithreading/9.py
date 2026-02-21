from threading import Event, Thread
import time

event = Event()

def waiter():
    print("Waiting...")
    event.wait()
    print("Triggered!")

def setter():
    time.sleep(3)
    event.set()

Thread(target=waiter).start()
Thread(target=setter).start()