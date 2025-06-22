class Job:
    def __init__(self,job_id,user_id,priority,arrival_time):
        self.job_id=job_id
        self.user_id = user_id
        self.priority= priority
        self.arrival_time = arrival_time
        self.wait_time = 0

    def __repr__(self):
        return f"Job({self.job_id},Priority = {self.priority}, Wait = {self.wait_time})"


class PrintQueueManager:
    def __init__(self,capacity=100):
        self.queue=[]
        self.capacity = capacity
        self.aging_interval =5
        self.max_priority =10

    def apply_priority_aging(self):
        for job in self.queue:
            if job.wait_time >=self.aging_interval and job.priority< self.max_priority:
                job.priority+=1
                job.wait_time=0
                print(f"[Aging] Job {job.job_id} promoted to priority {job.priority}")

        self.queue.sort(key=lambda  job:(-job.priority,job.arrival_time))

    def tick(self):
        for job in self.queue:
            job.wait_time+=1
        self.apply_priority_aging()

    def show_status(self):
        print("Current Queue State:")
        for job in self.queue:
            print(f"JobId:{job.job_id},User:{job.user_id},Priority:{job.priority},Wait:{job.wait_time}")