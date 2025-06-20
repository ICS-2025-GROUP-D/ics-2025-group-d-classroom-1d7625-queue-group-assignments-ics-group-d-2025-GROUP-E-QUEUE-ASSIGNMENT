import time
from core_queue_management import PrintJob, PrintQueue

class EventSimulator:
    def __init__(self, print_queue, aging_interval=5, aging_increment=1, expiry_limit=60):
        self.pq = print_queue
        self.aging_interval = aging_interval
        self.aging_increment = aging_increment
        self.expiry_limit = expiry_limit

    def tick(self):
        """Simulate a time tick: update job times, age priorities, remove expired jobs."""
        print("\n--- Tick ---")
        current_time = time.time()
        expired_indexes = []

        idx = self.pq.front
        for _ in range(self.pq.size):
            job = self.pq.queue[idx]

            if job:
                self._update_wait_time(job, current_time)
                self._apply_aging_if_due(job, current_time)
                if self._is_expired(job):
                    expired_indexes.append(idx)
                    print(f"[EXPIRE] Job {job.job_id} from user {job.user_id} expired after {job.waiting_time:.1f}s.")

            idx = (idx + 1) % self.pq.capacity

        self._remove_expired_jobs(expired_indexes)

    def _update_wait_time(self, job, current_time):
        job.waiting_time = current_time - job.enqueue_time

    def _apply_aging_if_due(self, job, current_time):
        if current_time - job.last_aging_time >= self.aging_interval:
            old_priority = job.priority
            job.priority += self.aging_increment
            job.last_aging_time = current_time
            print(f"[AGING] Job {job.job_id}: priority {old_priority} → {job.priority}")

    def _is_expired(self, job):
        return job.waiting_time >= self.expiry_limit

    def _remove_expired_jobs(self, expired_indexes):
        """Compact the queue by removing expired jobs."""
        if not expired_indexes:
            return

        new_queue = [None] * self.pq.capacity
        idx = self.pq.front
        new_idx = 0

        for _ in range(self.pq.size):
            job = self.pq.queue[idx]
            if job and idx not in expired_indexes:
                new_queue[new_idx] = job
                new_idx += 1
            idx = (idx + 1) % self.pq.capacity

        self.pq.queue = new_queue
        self.pq.front = 0
        self.pq.rear = new_idx - 1
        self.pq.size = new_idx
        
