 190376-ft-tick
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
=======
# this is a tester for the file
from queue_manager import PrintQueueManager, Job
def main():
    a=PrintQueueManager(capacity=5)
    a.queue.append(Job("J1", "user1", priority=2, arrival_time=0))
    a.queue.append(Job("J2", "user2", priority=3, arrival_time=1))
    a.queue.append(Job("J3", "user3", priority=1, arrival_time=2))

    print ("Initial Queue Status;")
    a.show_status()

    print("Simulating 6 time ticks (aging applies after 5)..." )
    for t in range(6):
        print(f"tick{t+1}---")
        a.tick()
        a.show_status()

    print ("Final Queue After aging")
    a.show_status()

if __name__== "__main__":
    main()
main
