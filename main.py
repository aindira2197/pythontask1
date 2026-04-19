import threading
import queue
import time
import random

class Producer(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        for i in range(10):
            item = random.randint(1, 100)
            self.q.put(item)
            print(f"{self.name} ishlab chiqardi: {item}")
            time.sleep(random.random())

class Consumer(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        while True:
            item = self.q.get()
            print(f"{self.name} olindi: {item}")
            self.q.task_done()
            time.sleep(random.random())

q = queue.Queue()

producer1 = Producer("Producer1", q)
producer2 = Producer("Producer2", q)
consumer1 = Consumer("Consumer1", q)
consumer2 = Consumer("Consumer2", q)

producer1.start()
producer2.start()
consumer1.start()
consumer2.start()

q.join()