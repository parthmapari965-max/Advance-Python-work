
import threading
import time

def task1():
    for i in range(1, 6):
        print("Task 1 - Counting:", i)
        time.sleep(1)

def task2():
    for i in range(1, 6):
        print("Task 2 - Counting:", i)
        time.sleep(1)

def task3():
    for i in range(1, 6):
        print("Task 3 - Counting:", i)
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for threads to finish
t1.join()
t2.join()
t3.join()

print("All tasks completed successfully!")