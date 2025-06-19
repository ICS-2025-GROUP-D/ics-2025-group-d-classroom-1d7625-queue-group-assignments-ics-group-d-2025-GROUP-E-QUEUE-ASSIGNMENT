import time


def update_waiting_time(self):
    """Update waiting time based on how long job has been in queue"""
    self.waiting_time = time.time() - self.enqueue_time

def should_age(self, aging_interval):
    """Check if this job should have its priority aged"""
    return (time.time() - self.last_aging_time) >= aging_interval

def age_priority(self, aging_increment=1):
    """Increase priority due to aging"""
    old_priority = self.priority
    self.priority += aging_increment
    self.last_aging_time = time.time()
    print(f"  [AGING] Job {self.job_id} priority: {old_priority} → {self.priority}")
    
def _apply_aging(self):
    """Apply aging to jobs that have waited long enough"""
    if self.is_empty():
        return
        
    aged_jobs = []
    idx = self.front
    for _ in range(self.size):
        job = self.queue[idx]
        if job and job.should_age(self.aging_interval):
            job.age_priority(self.aging_increment)
            aged_jobs.append(job.job_id)
        idx = (idx + 1) % self.capacity
    
    if aged_jobs:
        print(f"  [AGING] {len(aged_jobs)} job(s) received priority boost")

def _find_highest_priority_job(self):
    """Find the index of the highest priority job in the circular queue"""
    if self.is_empty():
        return -1
    
    # Update waiting times first
    idx = self.front
    for _ in range(self.size):
        job = self.queue[idx]
        if job:
            job.update_waiting_time()
        idx = (idx + 1) % self.capacity
    
    highest_priority = -1
    longest_wait_time = -1
    best_idx = self.front
    
    idx = self.front
    for _ in range(self.size):
        job = self.queue[idx]
        if job:
            # Check if this job has higher priority, or same priority but longer wait time
            if (job.priority > highest_priority or 
                (job.priority == highest_priority and job.waiting_time > longest_wait_time)):
                highest_priority = job.priority
                longest_wait_time = job.waiting_time
                best_idx = idx
        idx = (idx + 1) % self.capacity
    
    return best_idx

def show_aging_info(self):
    """Show detailed aging information"""
    print("\n" + "="*60)
    print("Aging Information:")
    print("="*60)
    print(f"Aging Interval: {self.aging_interval} seconds")
    print(f"Aging Increment: +{self.aging_increment} priority per age")
    
    if self.is_empty():
        print("[No jobs to age]")
        return
    
    current_time = time.time()
    print(f"\n{'Job ID':<8} {'Time Until Aging':<15} {'Times Aged':<10}")
    print("-" * 35)
    
    idx = self.front
    for _ in range(self.size):
        job = self.queue[idx]
        if job:
            time_since_aging = current_time - job.last_aging_time
            time_until_aging = max(0, self.aging_interval - time_since_aging)
            times_aged = job.priority - job.original_priority
            
            print(f"{job.job_id:<8} {time_until_aging:.1f}s{'':<6} {times_aged:<10}")
        idx = (idx + 1) % self.capacity

def force_aging(self):
    """Manually trigger aging for all jobs (useful for testing)"""
    print("\n[MANUAL AGING] Forcing aging for all jobs...")
    idx = self.front
    aged_count = 0
    for _ in range(self.size):
        job = self.queue[idx]
        if job:
            job.age_priority(self.aging_increment)
            aged_count += 1
        idx = (idx + 1) % self.capacity
    print(f"[MANUAL AGING] {aged_count} jobs aged")


            
            
            
        
        
        

    
    
        