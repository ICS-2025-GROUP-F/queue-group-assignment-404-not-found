from print_queue_manager import PrintQueueManager
import time

pq_manager = PrintQueueManager()

# Enqueue jobs individually
pq_manager.enqueue_job("Student", "Assignment Report", "J101", priority=1, expiry=5)
pq_manager.enqueue_job("Lecturer", "Exam Paper", "J102", priority=3, expiry=6)

# Simultaneous submissions (like a batch print request)
simultaneous_jobs = [
    ("Admin", "Transcript", "J103", 2, 5),
    ("Student", "Course Registration Form", "J104", 0, 4),
    ("Lecturer", "Lecture Notes", "J105", 1, 7)
]
pq_manager.handle_simultaneous_submissions(simultaneous_jobs)

# Run simulation ticks
for _ in range(6):
    pq_manager.tick()
    time.sleep(1)  # Simulate real passage of time
