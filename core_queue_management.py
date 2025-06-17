""" 1. Core Queue Management (Module Owner: Member 1)
Implement the circular queue data structure with fixed capacity.
Support enqueue, dequeue, and status operations.
Manage job metadata: user ID, job ID, priority, waiting time. """

class PrintJob: # represents a print job in the queue
    def __init__(self, user_id, job_id, priority):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = priority
        self.waiting_time = 0 # used to track how long the job has been in the queue

class PrintQueue: # represents the circular queue for the print jobs
    def __init__(self, capacity):
        self.capacity = capacity # maximum number of jobs the queue can have
        self.queue = [None] * capacity # the circular queue is initialized with None, with the size of the capacity
        self.front = 0
        self.rear = -1 # the first print job will be added at index 0 
        self.size = 0 # current number of jobs in the queue

    def is_full(self): # checks if the queue is full
        return self.size == self.capacity
    
    def is_empty(self): # checks if the queue is empty
        return self.size == 0
    
    def enqueue_job(self, user_id, job_id, priority):
        if self.is_full(): # a new job can't be added if the queue is full
            raise Exception("Queue is full, cannot add new print job.")
        new_job = PrintJob(user_id, job_id, priority)
        self.rear = (self.rear + 1) % self.capacity # move the rear pointer to the next index in a circular manner
        self.queue[self.rear] = new_job # add the new job at the rear of the print queue
        self.size += 1
        print(f"Job {job_id} from user {user_id} with priority {priority} successfully enqueued.")

    def dequeue_job(self):
        if self.is_empty(): # a job can't be removed from an empty queue
            raise Exception("Queue is empty, cannot remove print job.")
        job = self.queue[self.front] # jobs are removed from the front of the queue
        self.queue[self.front] = None # clear the job from the print queue
        self.front = (self.front + 1) % self.capacity # move the front pointer to the next index in a circular manner
        self.size -= 1
        print(f"Job {job.job_id} from user {job.user_id} successfully dequeued.")
        return job
    
    def show_status(self):
        print("Current Print Queue Status:")
        if self.is_empty():
            print("[Empty Queue]")
        idx = self.front
        for _ in range(self.size): # Go through the current print jobs in the queue
            job = self.queue[idx]
            print(f"Job ID: {job.job_id}, User ID: {job.user_id}, Priority: {job.priority}, Waiting Time: {job.waiting_time}")
            idx = (idx + 1) % self.capacity # move to the next job in the circular queue

if __name__ == "__main__":
    pq = PrintQueue(3)
    pq.enqueue_job("user1", "job001", 2)
    pq.enqueue_job("user2", "job002", 4)
    pq.show_status()
    pq.dequeue_job()
    pq.enqueue_job("user3", "job003", 5)
    pq.enqueue_job("user4", "job004", 1)  # should raise "Queue is full" if working
    pq.show_status()