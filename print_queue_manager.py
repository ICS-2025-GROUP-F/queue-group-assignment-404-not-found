import tkinter as tk
from tkinter import ttk
import csv

class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.tick_count = 0

    def enqueue_job(self, user_role, document_type, job_id, priority, expiry):
        job = {
            'user_role': user_role,
            'document_type': document_type,
            'job_id': job_id,
            'priority': priority,
            'wait_time': 0,
            'expiry': expiry,
            'processed': False
        }
        self.queue.append(job)
        print(f"📥 {user_role} submitted '{document_type}' (Job {job_id}) | Priority: {priority}, Expires in: {expiry} ticks")

    def print_job(self):
        if self.queue:
            job = self.queue.pop(0)
            job['processed'] = True
            print(f"🖨️ PRINTED: {job['document_type']} (Job {job['job_id']}) from {job['user_role']}")
        else:
            print("⚠️ No jobs to print.")

    def apply_priority_aging(self):
        for job in self.queue:
            if job['wait_time'] % 3 == 0 and job['wait_time'] > 0:
                job['priority'] += 1
                print(f"🔼 PRIORITY AGED: Job {job['job_id']} now has priority {job['priority']}")

    def remove_expired_jobs(self):
        expired = [job for job in self.queue if job['wait_time'] >= job['expiry']]
        for job in expired:
            self.queue.remove(job)
            print(f"❌ EXPIRED: {job['document_type']} (Job {job['job_id']}) from {job['user_role']}")

    def handle_simultaneous_submissions(self, jobs):
        for job in jobs:
            self.enqueue_job(*job)

    def tick(self):
        self.tick_count += 1
        print(f"\n🕒 Tick {self.tick_count}: Time advanced.")

        for job in self.queue:
            job['wait_time'] += 1

        self.apply_priority_aging()
        self.remove_expired_jobs()
        self.queue.sort(key=lambda j: j['priority'], reverse=True)

        if self.tick_count % 2 == 0:
            self.print_job()

        self.export_status_to_csv()
        self.show_status()

    def export_status_to_csv(self):
        filename = f"printer_log_tick_{self.tick_count}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Job ID", "User Role", "Document Type", "Priority", "Wait Time", "Expires In"])
            for job in self.queue:
                writer.writerow([
                    job['job_id'],
                    job['user_role'],
                    job['document_type'],
                    job['priority'],
                    job['wait_time'],
                    job['expiry'] - job['wait_time']
                ])
        print(f"📄 Exported log to {filename}")

    def show_status(self):
        window = tk.Tk()
        window.title(f"Printer Queue - Tick {self.tick_count}")
        table = ttk.Treeview(window)
        table["columns"] = ("Job ID", "User Role", "Document Type", "Priority", "Wait Time", "Expires In")

        for col in table["columns"]:
            table.heading(col, text=col)
            table.column(col, width=100, anchor=tk.CENTER)

        for job in self.queue:
            table.insert("", "end", values=(
                job['job_id'],
                job['user_role'],
                job['document_type'],
                job['priority'],
                job['wait_time'],
                job['expiry'] - job['wait_time']
            ))

        table.pack(expand=True, fill='both')
        window.mainloop()
