import threading

class PrintQueueManager:
    def __init__(self,queue):
        self.queue = queue
        self.current_time = 0
        self.lock = None

    def init_concurrency(self):
        self.lock = threading.Lock()

    def add_job(self, user_id, job_id, priority, max_wait_time=10):
        job = {
            'user_id' : user_id,
            'job_id' : job_id,
            'priority' : priority,
            'submit_time' : self.current_time,
            'max_wait_time' : max_wait_time
        }
        if self.lock:
            with self.lock:
                self.queue.append(job)
        else:
            self.queue.append(job)

    def remove_expired_jobs(self):
        if not self.queue:
            return

        expired_jobs = self._find_expired_jobs()
        self._process_expired_jobs(expired_jobs)

    def _find_expired_jobs(self):
        current_time = self.current_time
        return [job for job in self.queue
                if current_time - job['submit_time'] >= job['max_wait_time']]

    def _process_expired_jobs(self,expired_jobs):
        if self.lock:
            with self.lock:
                self._remove_jobs(expired_jobs)
        else:
            self._remove_jobs(expired_jobs)

    def _remove_jobs(self,jobs):
        for job in jobs:
            self.queue.remove(job)
            wait_time = self.current_time - job['submit_time']
            print(f"[EXPIRED] Job {job['job_id']} (Priority {job['priority']})"
                  f"from User {job['user_id']} expired after {wait_time}ticks")

    def tick(self):
        self.current_time +=1
        self.remove_expired_jobs()

if __name__ == "__main__":
    shared_queue = []
    pq = PrintQueueManager(shared_queue)

    pq.init_concurrency()

    pq.add_job("user1", 1, priority=3, max_wait_time=5)
    pq.add_job("user2",2, priority=1, max_wait_time=10)
    pq.add_job("user3", 3, priority=2,max_wait_time=3)

    print("\n=== simulation started ===")
    for t in range(1,13):
        pq.current_time = t
        print(f"\n[Time {t}] Queue: {len(pq.queue)} jobs")
        pq.remove_expired_jobs()
        pq.tick()

