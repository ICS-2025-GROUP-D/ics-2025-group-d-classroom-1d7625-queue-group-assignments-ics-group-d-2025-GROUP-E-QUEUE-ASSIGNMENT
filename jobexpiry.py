from core_queue_management import print_queue
class JobExpiryCleanup:
    def __init__(self):
        self.pq=print_queue
        self.expiry_time=60
        self.expired_jobs=[]

    
    def tick(self):
        index=self.pq.front
        for _ in range(self.pq.size):
            job= self.pq.queue[index]
            if job:
                job.waiting_time +=1
            index=(index+1)% self.pq.capacity
        self.remove_expired_jobs

    def remove_expired_jobs(self):
        job_expired_list=[None]*self.pq.capacity
        index=self.pq.front
        count=0
        new_front=0
        for _ in range(self.pq.size):
            job = self.pq.queue[index]
            if job and job.waiting_time >= self.expiry_time:
                self.expired_jobs.append(job)
                print(f"Job {job.job_id} from user {job.user_id} has expired and will be removed.")
            else:
                job_expired_list[new_front] = job
                new_front += 1
            index= (index+1)% self.pq.capacity
        self.pq.queue= job_expired_list
        self.pq.front=new_front
        self.pq.size = count
        self.pq.rear=(new_front+count -1)%self.pq.capacity if count >0 else -1
        

       



   