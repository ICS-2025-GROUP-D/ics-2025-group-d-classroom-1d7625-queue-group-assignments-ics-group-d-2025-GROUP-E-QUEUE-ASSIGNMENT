import tkinter as tk
from tkinter import ttk
import time

# Import simulation modules
from core_queue_management import PrintQueue, PrintJob
from priority_aging import (
    initialize_queue_for_aging,
    update_all_waiting_times,
    apply_aging,
    find_highest_priority_job,
    show_aging_info,
    force_aging
)
from Concurrent_Job_submission_handling import send_simultaneous

class PrintQueueVisualiser:
    def __init__(self, root, print_queue):
        self.print_queue = print_queue
        self.root = root
        self.root.title("📠 Print Queue Visualizer")
        self.root.geometry("600x350")
        self.root.resizable(False, False)

        # Table for jobs
        self.tree = ttk.Treeview(root, columns=("Job ID", "User ID", "Priority", "Waiting Time"), show="headings")
        self.tree.pack(fill="both", expand=True)

        for col in ("Job ID", "User ID", "Priority", "Waiting Time"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Refresh Queue", command=self.refresh_queue).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Run Simulation", command=self.run_simulation).pack(side="left", padx=10)

        self.refresh_queue()

    def refresh_queue(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        if self.print_queue.is_empty():
            self.tree.insert("", "end", values=("EMPTY", "", "", ""))
        else:
            idx = self.print_queue.front
            for _ in range(self.print_queue.size):
                job = self.print_queue.queue[idx]
                self.tree.insert("", "end", values=(
                    job.job_id,
                    job.user_id,
                    job.priority,
                    f"{job.waiting_time:.1f}s"
                ))
                idx = (idx + 1) % self.print_queue.capacity

    def run_simulation(self):
        # Full simulation logic from main.py, condensed here
        print("\n=== Running Queue Simulation ===")
        self.print_queue = PrintQueue(5)
        initialize_queue_for_aging(self.print_queue, aging_interval=5, aging_increment=1)

        self.print_queue.enqueue_job("user1", "job001", 2)
        self.print_queue.enqueue_job("user2", "job002", 4)
        time.sleep(2)
        update_all_waiting_times(self.print_queue)

        self.print_queue.enqueue_job("user3", "job003", 5)
        time.sleep(3)

        try:
            self.print_queue.enqueue_job("user4", "job004", 1)
        except Exception as e:
            print(f"Error: {e}")

        update_all_waiting_times(self.print_queue)
        self.print_queue.dequeue_job()
        self.print_queue.enqueue_job("user4", "job004", 1)

        print("\n--- Applying Automatic Aging ---")
        time.sleep(6)
        apply_aging(self.print_queue)
        update_all_waiting_times(self.print_queue)

        print("\n--- Force Aging ---")
        force_aging(self.print_queue)
        update_all_waiting_times(self.print_queue)

        print("\n--- Concurrent Submission ---")
        jobs = [
            PrintJob("user1", "job001", 2),
            PrintJob("user2", "job002", 4),
            PrintJob("user3", "job003", 5),
            PrintJob("user4", "job004", 1)
        ]
        send_simultaneous(self.print_queue, jobs)

        print("\n--- Simulation Complete ---")
        self.refresh_queue()
