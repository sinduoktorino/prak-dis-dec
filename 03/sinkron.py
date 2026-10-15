import threading
import time

def task(name, delay):
    print(f"Task {name} starting...")
    time.sleep(delay)
    print(f"Task {name} finished after {delay}s.")

t1 = threading.Thread(target=task, args=("A", 5))
t2 = threading.Thread(target=task, args=("B", 5))
t3 = threading.Thread(target=task, args=("C", 5))
t4 = threading.Thread(target=task, args=("D", 5))
t5 = threading.Thread(target=task, args=("E", 5))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("All tasks completed.")


### 2. Contoh Data Race / Race Conditions (`race-conditions-01.py`)

import time
from threading import Thread

balance = 100

def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(0.01)
        balance -= amount
        print(f"Mengambil sejumlah Rp {amount}. Saldo: Rp {balance}")

t1 = Thread(target=withdraw, args=(80,))
t2 = Thread(target=withdraw, args=(80,))

t1.start()
t2.start()
t1.join()
t2.join()

### 3. Contoh Pencegahan Data Race dengan Lock (`race-conditions-02.py`)

import time
from threading import Thread
import threading

balance = 100
counter_lock = threading.Lock()

def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(0.01)
        with counter_lock:
            balance -= amount
            print(f"Mengambil sejumlah Rp {amount}. Saldo: Rp {balance}")

t1 = Thread(target=withdraw, args=(80,))
t2 = Thread(target=withdraw, args=(80,))

t1.start()
t2.start()
t1.join()
t2.join()




# ### 4. Contoh Kondisi Deadlock (`deadlock-01.py`)

# import threading
# import time

# lock_a = threading.Lock()
# lock_b = threading.Lock()

# def thread_task1():
#     with lock_a:
#         print("Thread 1: Locked A, waiting for B...")
#         time.sleep(1)
#         with lock_b:
#             print("Thread 1: Locked both")

# def thread_task2():
#     with lock_b:
#         print("Thread 2: Locked B, waiting for A...")
#         time.sleep(1)
#         with lock_a:
#             print("Thread 2: Locked both")

# t1 = threading.Thread(target=thread_task1)
# t2 = threading.Thread(target=thread_task2)

# t1.start()
# t2.start()
# t1.join()
# t2.join()



### 5. Contoh Pencegahan Deadlock dengan Timeout (`deadlock-02.py`)

import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_task():
    if lock_a.acquire(timeout=5):
        try:
            print("Thread 1: Acquired Lock A")
            time.sleep(1)
            print("Thread 1: Waiting for Lock B...")
        finally:
            lock_a.release()
            
    if lock_b.acquire(timeout=5):
        try:
            print("Thread 1: Acquired Lock B")
        finally:
            lock_b.release()

def thread2_task():
    if lock_b.acquire(timeout=5):
        try:
            print("Thread 2: Acquired Lock B")
            time.sleep(1)
            print("Thread 2: Waiting for Lock A...")
        finally:
            lock_b.release()
            
    if lock_a.acquire(timeout=5):
        try:
            print("Thread 2: Acquired Lock A")
        finally:
            lock_a.release()

t1 = threading.Thread(target=thread1_task)
t2 = threading.Thread(target=thread2_task)

t1.start()
t2.start()
t1.join()
t2.join()
print("Execution Finished")