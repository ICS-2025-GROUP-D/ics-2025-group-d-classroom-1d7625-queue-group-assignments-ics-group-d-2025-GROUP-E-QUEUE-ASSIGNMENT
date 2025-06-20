import tkinter as tk
from tkinter import ttk

class PrintQueueManager:
    def __init__(self):
        self.queue = []  # This must be filled by other modules

    def show_status_gui(self):
        window = tk.Tk()
        window.title("Print Queue Visualizer")
        window.geometry("700x450")
        window.configure(bg="#ffe6f0")

        title_label = tk.Label(
            window,
            text="Print Queue Snapshot",
            font=("Segoe UI", 20, "bold"),
            bg="#ffe6f0",
            fg="#a83279"
        )
        title_label.pack(pady=15)

        frame = tk.Frame(window, bg="#ffd6eb", bd=2, relief=tk.GROOVE)
        frame.pack(padx=25, pady=10, fill=tk.BOTH, expand=True)

        columns = ("User ID", "Job ID", "Priority", "Waiting Time")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=8)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER, width=130)

        for job in self.queue:
            tree.insert("", tk.END, values=(job.user_id, job.job_id, job.priority, job.waiting_time))

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#fff0f5",
                        foreground="#4b004f",
                        fieldbackground="#ffd6eb",
                        rowheight=30,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 11, "bold"),
                        background="#f7b6d2",
                        foreground="#4b004f")

        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        refresh_btn = tk.Button(
            window,
            text="🔄 Refresh View",
            command=lambda: self.refresh_gui(window),
            font=("Segoe UI", 11),
            bg="#f9c0d8",
            fg="#4b004f",
            padx=10,
            pady=5
        )
        refresh_btn.pack(pady=12)

        window.mainloop()

    def refresh_gui(self, window):
        window.destroy()
        self.show_status_gui()
