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
        print("tick{t+1}---")
        a.tick()
        a.show_status()

    print ("Final Queue After aging")
    a.show_status()

if __name__== "__main__":
    main()
