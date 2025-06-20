class PrintQueueManager:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue_job(self, user_id, job_id, priority):
        if self.size == self.capacity:
            return "Queue is full"

        job = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }

        self.queue[self.rear] = job
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return "Job added"

    def dequeue_job(self):
        if self.size == 0:
            return "Queue is empty"

        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return job

    def show_status(self):
        result = []
        index = self.front
        count = 0

        while count < self.size:
            result.append(self.queue[index])
            index = (index + 1) % self.capacity
            count += 1

        return result

    def get_status(self):
        # For use in unit tests
        return self.show_status()
