from collections import deque

class Job:
    def __init__(self, user_id, job_id, priority, timestamp):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = priority
        self.waiting_time = 0
        self.timestamp = timestamp

    def __repr__(self):
        return f"Job(user={self.user_id}, id={self.job_id}, priority={self.priority}, waiting={self.waiting_time})"

class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = deque(maxlen=capacity)
        self.system_time = 0

    def enqueue_job(self, user_id, job_id, priority):
        if len(self.queue) >= self.capacity:
            print(f"[ENQUEUE FAILED] Queue full. Job {job_id} not added.")
            return
        job = Job(user_id, job_id, priority, self.system_time)
        self.queue.append(job)
        print(f"[ENQUEUE] Job {job_id} added to queue.")

    def dequeue_job(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"[DEQUEUE] Job {job.job_id} removed from queue.")
        else:
            print("[DEQUEUE FAILED] Queue is empty.")

    def show_status(self):
        print("\n[QUEUE STATUS]")
        if not self.queue:
            print("Queue is empty.")
        else:
            for i, job in enumerate(self.queue, start=1):
                print(f"{i}. {job}")
