import threading
from queue import Queue;
from core_queue_management import PrintQueue, PrintJob  #importing the PrintQueue and PrintJob classes

def enqueue_job(self, user_id, job_id, priority):
    # Addition aof a print job to the queue
    with self.lock:
        if self.is_full():
            raise Exception("Queue is full, cannot add new print job.")
        new_job = PrintJob(user_id, job_id, priority)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = new_job
        self.size += 1
        print(f"Job {job_id} from user {user_id} with priority {priority} successfully enqueued.")
        
    
def dequeue(self):
    with self.lock: #locking added for thread safety
        if self.is_empty():
            raise Exception("Queue is empty, cannot remove print job.")
        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Job {job.job_id} from user {job.user_id} successfully dequeued.")
    return job 
def size(self):
    
    """Get the number of jobs in the queue."""
    return self.queue.qsize()
def send_simultaneous(print_queue, jobs):
    
    """Send multiple jobs to the queue simultaneously."""
    threads = []
    for job in jobs:
        t = threading.Thread(target=print_queue.enqueue_job, args=(job.user_id, job.job_id, job.priority))
        threads.append(t)
        t.start()
    for t in threads:
         t.join() # Ensure all jobs are enqueued        
  