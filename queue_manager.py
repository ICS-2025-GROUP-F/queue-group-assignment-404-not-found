from dataclasses import dataclass
from typing import List, Optional #for the circular buffer

@dataclass #ensures a cleaner version of the code and also use fewer lines of code
class PrintJob: #defines a print job using dataclass which automatically creates a constructor
    user_id: str #who sent the print job
    job_id: str  #unique job name/number
    priority: int  #an integer value to indicate the urgency of the job
    waiting_time: int = 0 #shows how long a job has been in the queue

class CircularQueue: #is a circular buffer - behaves like a queue but the list(memory) is reused in a loop
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.buffer: List[Optional[PrintJob]] = [None] * capacity #a fixed size list to hold jobs
        self.front = 0  #shows where to remove the next job
        self.rear = -1  #shows where the last job was added
        self.size = 0   #shows the current number of jobs

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def enqueue(self, job: PrintJob) ->bool: #adds a job to the queue
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.capacity #increasing the rear in a circular way - queue reaches the end of the list, it wraps back to the beginning
        self.buffer[self.rear] = job #insert a job into the buffer at the rear
        self.size += 1 #increase the size
        return True   #return False if queue is full

    def dequeue(self) -> Optional[PrintJob]:
        if self.is_empty():
            return None
        job = self.buffer[self.front]  #removes the next job from the front of the queue
        self.buffer[self.front] = None
        self.front = (self.front +1) % self.capacity
        self.size -= 1
        return job

    def snapshot(self) -> List[PrintJob]: #return a read-only list of all jobs in queue order(front-rear)
        items = []
        index = self.front
        for _ in range(self.size):
            items.append(self.buffer[index])
            index = (index +1) % self.capacity

        return items

class PrintQueueManager: #class that will be called to manage the print queue
    def __init__(self, capacity: int = 100):
        self.queue = CircularQueue(capacity)

    def enqueue_job(self, user_id: str, job_id: str, priority: int) -> None: #creates a new print job
        job = PrintJob(user_id, job_id, priority)
        if not self.queue.enqueue(job):
            raise OverflowError("Queue full - cannot accept any new job")

    def print_job(self) -> Optional[PrintJob]: #removes and returns the next job from the queue
        return self.queue.dequeue()

    def show_status(self) -> None:
        print("\n--- Queue status ---")
        for pos, job in enumerate(self.queue.snapshot(), start=1): #pos: position in queue
            print(f"{pos:02d} | User:{job.user_id} Job:{job.job_id} "f"P:{job.priority} Wait:{job.waiting_time}")
        if self.queue.is_empty():
            print("(queue is empty)")
            print("-----------------------\n")
