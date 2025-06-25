import threading

class PrintQueueManager:
    def __init__(self):
        # Initialize an empty queue; should be replaced with the team's actual circular queue implementation.
        self.queue = []
        # A lock to ensure that only one thread can access the enqueue operation at a time (thread safety).
        self.lock = threading.Lock()

    def enqueue_job(self, user_id, job_id, priority):
        """
        This is a placeholder for the core queue's enqueue function.
        It simulates adding a print job to the queue.
        In the final system, this should call the actual enqueue method from Module 1 (circular queue).
        """
        job = {
            "user_id": user_id,
            "job_id": job_id,       # e.g., 'job_01'
            "priority": priority,
            "waiting_time": 0       # Initialize waiting time at submission
        }
        # Simulate adding the job to the queue (non-thread-safe placeholder).
        self.queue.append(job)  # Replace with actual enqueue logic from Module 1.
        print(f"[ENQUEUED] Job {job_id} from {user_id} with priority {priority}")

    def _submit_job_threadsafe(self, job):
        """
        Internal method to safely submit a job to the queue using a lock.
        Ensures mutual exclusion when multiple threads attempt to enqueue jobs concurrently.
        """
        with self.lock:
            self.enqueue_job(
                user_id=job["user_id"],
                job_id=job["job_id"],
                priority=job["priority"]
            )

    def handle_simultaneous_submissions(self, jobs):
        """
        Handles the 'send_simultaneous' event: simulates multiple users submitting print jobs at the same time.
        Spawns a thread for each job submission to mimic real-world concurrency.
        Ensures thread-safe enqueuing using locks.
        
        Parameters:
        - jobs: A list of job dictionaries, each containing 'user_id', 'job_id', and 'priority'.
        """
        threads = []

        # Create and start a thread for each job submission
        for job in jobs:
            t = threading.Thread(target=self._submit_job_threadsafe, args=(job,))
            threads.append(t)
            t.start()

        # Wait for all job submissions to complete
        for t in threads:
            t.join()

        print("[INFO] All simultaneous job submissions completed.")
