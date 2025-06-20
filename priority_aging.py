import time

def initialize_job_for_aging(job):
    """Initialize job with additional attributes needed for aging functionality"""
    if not hasattr(job, 'original_priority'):
        job.original_priority = job.priority
    if not hasattr(job, 'enqueue_time'):
        job.enqueue_time = time.time()
    if not hasattr(job, 'last_aging_time'):
        job.last_aging_time = time.time()

def initialize_queue_for_aging(queue, aging_interval=30, aging_increment=1):
    """Initialize queue with aging parameters"""
    queue.aging_interval = aging_interval
    queue.aging_increment = aging_increment

def update_waiting_time(job):
    """Update waiting time based on how long job has been in queue"""
    initialize_job_for_aging(job)  # Ensure job has required attributes
    job.waiting_time = time.time() - job.enqueue_time

def should_age(job, aging_interval):
    """Check if this job should have its priority aged"""
    initialize_job_for_aging(job)  # Ensure job has required attributes
    return (time.time() - job.last_aging_time) >= aging_interval

def age_priority(job, aging_increment=1):
    """Increase priority due to aging"""
    initialize_job_for_aging(job)  # Ensure job has required attributes
    old_priority = job.priority
    job.priority += aging_increment
    job.last_aging_time = time.time()
    print(f"  [AGING] Job {job.job_id} priority: {old_priority} → {job.priority}")

def apply_aging(queue):
    """Apply aging to jobs that have waited long enough"""
    if queue.is_empty():
        return
    
    # Initialize queue for aging if not already done
    if not hasattr(queue, 'aging_interval'):
        initialize_queue_for_aging(queue)
         
    aged_jobs = []
    idx = queue.front
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job and should_age(job, queue.aging_interval):
            age_priority(job, queue.aging_increment)
            aged_jobs.append(job.job_id)
        idx = (idx + 1) % queue.capacity
     
    if aged_jobs:
        print(f"  [AGING] {len(aged_jobs)} job(s) received priority boost")

def find_highest_priority_job(queue):
    """Find the index of the highest priority job in the circular queue"""
    if queue.is_empty():
        return -1
     
    # Update waiting times first
    idx = queue.front
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job:
            update_waiting_time(job)
        idx = (idx + 1) % queue.capacity
     
    highest_priority = -1
    longest_wait_time = -1
    best_idx = queue.front
     
    idx = queue.front
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job:
            # Check if this job has higher priority, or same priority but longer wait time
            if (job.priority > highest_priority or
                 (job.priority == highest_priority and job.waiting_time > longest_wait_time)):
                highest_priority = job.priority
                longest_wait_time = job.waiting_time
                best_idx = idx
        idx = (idx + 1) % queue.capacity
     
    return best_idx

def update_all_waiting_times(queue):
    """Update waiting times for all jobs in the queue"""
    if queue.is_empty():
        return
    
    idx = queue.front
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job:
            update_waiting_time(job)
        idx = (idx + 1) % queue.capacity

def show_aging_info(queue):
    """Show detailed aging information"""
    # Initialize queue for aging if not already done
    if not hasattr(queue, 'aging_interval'):
        initialize_queue_for_aging(queue)
        
    print("\n" + "="*60)
    print("Aging Information:")
    print("="*60)
    print(f"Aging Interval: {queue.aging_interval} seconds")
    print(f"Aging Increment: +{queue.aging_increment} priority per age")
     
    if queue.is_empty():
        print("[No jobs to age]")
        return
     
    current_time = time.time()
    print(f"\n{'Job ID':<8} {'Time Until Aging':<15} {'Times Aged':<10}")
    print("-" * 35)
     
    idx = queue.front
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job:
            initialize_job_for_aging(job)  # Ensure job has required attributes
            time_since_aging = current_time - job.last_aging_time
            time_until_aging = max(0, queue.aging_interval - time_since_aging)
            times_aged = job.priority - job.original_priority
                     
            print(f"{job.job_id:<8} {time_until_aging:.1f}s{'':<6} {times_aged:<10}")
        idx = (idx + 1) % queue.capacity

def force_aging(queue):
    """Manually trigger aging for all jobs (useful for testing)"""
    # Initialize queue for aging if not already done
    if not hasattr(queue, 'aging_increment'):
        initialize_queue_for_aging(queue)
        
    print("\n[MANUAL AGING] Forcing aging for all jobs...")
    idx = queue.front
    aged_count = 0
    for _ in range(queue.size):
        job = queue.queue[idx]
        if job:
            age_priority(job, queue.aging_increment)
            aged_count += 1
        idx = (idx + 1) % queue.capacity
    print(f"[MANUAL AGING] {aged_count} jobs aged")