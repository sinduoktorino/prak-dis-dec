class VectorClock:
    def __init__(self, num_processes, process_id):
        self.clocks = [0] * num_processes
        self.process_id = process_id

    def increment(self):
        self.clocks[self.process_id] += 1

    def send_message(self):
        self.increment()
        return list(self.clocks)

    def receive_message(self, received_clocks):
        for i in range(len(self.clocks)):
            self.clocks[i] = max(self.clocks[i], received_clocks[i])
        self.increment()

    def __str__(self):
        return f"P{self.process_id}: {self.clocks}"

    def happens_before(self, other_vector_clock):
        if self.clocks == other_vector_clock.clocks:
            return False

        all_le = True
        any_lt = False

        for i in range(len(self.clocks)):
            if self.clocks[i] > other_vector_clock.clocks[i]:
                return False
            if self.clocks[i] < other_vector_clock.clocks[i]:
                any_lt = True

        return all_le and any_lt

    def is_concurrent(self, other_vector_clock):
        return not (self.happens_before(other_vector_clock) or 
                    other_vector_clock.happens_before(self))

vc0 = VectorClock(num_processes=3, process_id=0)
vc1 = VectorClock(num_processes=3, process_id=1)
vc2 = VectorClock(num_processes=3, process_id=2)

print(vc0)
print(vc1)
print(vc2)

vc0.increment()
print(vc0)

message_from_p0 = vc0.send_message()
vc1.receive_message(message_from_p0)
print(vc0)
print(vc1)

vc2.increment()
print(vc2)

message_from_p1 = vc1.send_message()
vc2.receive_message(message_from_p1)
print(vc1)
print(vc2)

print(f"vc0 happens before vc1: {vc0.happens_before(vc1)}")
print(f"vc1 happens before vc0: {vc1.happens_before(vc0)}")
print(f"vc0 is concurrent with vc2: {vc0.is_concurrent(vc2)}")

# import threading
# import time

# def task(name, delay):
#     print(f"Task {name} starting...")
#     time.sleep(delay)
#     print(f"Task {name} finished after {delay}s.")

# t1 = threading.Thread(target=task, args=("A", 5))
# t2 = threading.Thread(target=task, args=("B", 5))
# t3 = threading.Thread(target=task, args=("C", 5))
# t4 = threading.Thread(target=task, args=("D", 5))
# t5 = threading.Thread(target=task, args=("E", 5))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# print("All tasks completed.")


# ### 2. Contoh Data Race / Race Conditions (`race-conditions-01.py`)

# import time
# from threading import Thread

# balance = 100

# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         time.sleep(0.01)
#         balance -= amount
#         print(f"Mengambil sejumlah Rp {amount}. Saldo: Rp {balance}")

# t1 = Thread(target=withdraw, args=(80,))
# t2 = Thread(target=withdraw, args=(80,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# ### 3. Contoh Pencegahan Data Race dengan Lock (`race-conditions-02.py`)

# import time
# from threading import Thread
# import threading

# balance = 100
# counter_lock = threading.Lock()

# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         time.sleep(0.01)
#         with counter_lock:
#             balance -= amount
#             print(f"Mengambil sejumlah Rp {amount}. Saldo: Rp {balance}")

# t1 = Thread(target=withdraw, args=(80,))
# t2 = Thread(target=withdraw, args=(80,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()




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



# ### 5. Contoh Pencegahan Deadlock dengan Timeout (`deadlock-02.py`)

# import threading
# import time

# lock_a = threading.Lock()
# lock_b = threading.Lock()

# def thread1_task():
#     if lock_a.acquire(timeout=5):
#         try:
#             print("Thread 1: Acquired Lock A")
#             time.sleep(1)
#             print("Thread 1: Waiting for Lock B...")
#         finally:
#             lock_a.release()
            
#     if lock_b.acquire(timeout=5):
#         try:
#             print("Thread 1: Acquired Lock B")
#         finally:
#             lock_b.release()

# def thread2_task():
#     if lock_b.acquire(timeout=5):
#         try:
#             print("Thread 2: Acquired Lock B")
#             time.sleep(1)
#             print("Thread 2: Waiting for Lock A...")
#         finally:
#             lock_b.release()
            
#     if lock_a.acquire(timeout=5):
#         try:
#             print("Thread 2: Acquired Lock A")
#         finally:
#             lock_a.release()

# t1 = threading.Thread(target=thread1_task)
# t2 = threading.Thread(target=thread2_task)

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Execution Finished")
