""" 6. Visualization & Reporting
Create clear, user-friendly visual snapshots of the queue state after each event.
Format output to show job details in print order.
Optionally, design a simple GUI or web interface (extra credit). """

import tkinter as tk # library for creating the GUI
from tkinter import ttk # library for creating themed widgets

class PrintQueueVisualiser:
    def __init(self, root, print_queue):
        self.print_queue = print_queue
        self.root = root # the base window for the GUI
        self.root.title("Print Queue Visualiser") # the title of the widget
        self.tree = ttk.Treeview(root, columns=("Job ID", "User ID", "Priority", "Waiting Time"), show="headings") # create the columns for the treeview widget
        self.tree.pack(fill="both", expand=True) # create a treeview widget to display the print jobs

        for col in ("Job ID", "User ID", "Priority", "Waiting Time"):
            self.tree.heading(col, text=col)

        self.refresh_button = ttk.Button(root, text="Refresh", command=self.refresh_queue) # create a button to refresh the print queue display
        self.refresh_button.pack(pady=10) # style the button and add it to the window

    def refresh_queue(self):
        for row in self.tree.get_children(): # clear the existing rows in the treeview
            self.tree.delete(row)
        
        if self.queue.is_empty(): # check if the print queue is empty
            self.tree.insert("", "end", values=("Print queue is empty", "", "", ""))
        else:
            idx = self.queue.front
            for _ in range(self.queue.size): # loop through the print queue
                job = self.queue.queue[idx]
                self.tree.insert("", "end", values=(job.job_id, job.user_id, job.priority, f"{job.waiting_time:.1f}s")) 
                idx = (idx + 1) % self.queue.capacity

