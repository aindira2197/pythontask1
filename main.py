import threading
import queue
import time
import random

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(1, 100)
            self.queue.put(item)
            print(f"Produced {item}")
            time.sleep(random.random())

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = self.queue.get()
            print(f"Consumed {item}")
            time.sleep(random.random())
            self.queue.task_done()

q = queue.Queue()

producer = Producer(q)
consumer = Consumer(q)

producer.start()
consumer.start()

producer.join()
consumer.join()

print("All tasks are done") 

class SharedQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.queue.put(item)

    def get(self):
        with self.lock:
            return self.queue.get()

shared_q = SharedQueue()

def producer_task(q):
    for i in range(10):
        item = random.randint(1, 100)
        q.put(item)
        print(f"Produced {item}")
        time.sleep(random.random())

def consumer_task(q):
    for i in range(10):
        item = q.get()
        print(f"Consumed {item}")
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer_task, args=(shared_q,))
consumer_thread = threading.Thread(target=consumer_task, args=(shared_q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All tasks are done")

class ProducerConsumer:
    def __init__(self, queue):
        self.queue = queue

    def produce(self, item):
        self.queue.put(item)

    def consume(self):
        return self.queue.get()

pc = ProducerConsumer(queue.Queue())

def producer_task(pc):
    for i in range(10):
        item = random.randint(1, 100)
        pc.produce(item)
        print(f"Produced {item}")
        time.sleep(random.random())

def consumer_task(pc):
    for i in range(10):
        item = pc.consume()
        print(f"Consumed {item}")
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer_task, args=(pc,))
consumer_thread = threading.Thread(target=consumer_task, args=(pc,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All tasks are done")