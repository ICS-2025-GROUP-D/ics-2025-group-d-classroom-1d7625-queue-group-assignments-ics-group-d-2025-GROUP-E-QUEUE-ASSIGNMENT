import time
from core_queue_management import PrintQueue
from priority_aging import (
    initialize_queue_for_aging, 
    update_all_waiting_times, 
    apply_aging, 
    find_highest_priority_job, 
    show_aging_info, 
    force_aging
)

if __name__ == "__main__":
    # Create queue and initialize it for aging functionality
    pq = PrintQueue(3)
    initialize_queue_for_aging(pq, aging_interval=5, aging_increment=1)  # 5 seconds for demo
    
    print("=== Basic Queue Operations ===")
    pq.enqueue_job("user1", "job001", 2)
    pq.enqueue_job("user2", "job002", 4)
    
    print("\n--- Waiting 2 seconds ---")
    time.sleep(2)
    
    # Update waiting times and show status
    update_all_waiting_times(pq)
    pq.show_status()
    
    # Fill the queue completely
    pq.enqueue_job("user3", "job003", 5)  # This fills the queue (size = 3)
    
    print("\n--- Waiting another 3 seconds ---")
    time.sleep(3)
    
    # This should raise "Queue is full" error
    try:
        pq.enqueue_job("user4", "job004", 1)
    except Exception as e:
        print(f"Error: {e}")
    
    # Update waiting times and show status
    update_all_waiting_times(pq)
    pq.show_status()
    
    # Now dequeue one to make space and try again
    print("\n--- Dequeuing one job to make space ---")
    pq.dequeue_job()
    pq.enqueue_job("user4", "job004", 1)  # This should work now
    
    print("\n=== Advanced Priority Features ===")
    
    # Update waiting times and show current status
    update_all_waiting_times(pq)
    pq.show_status()
    
    # Show aging information
    print("\n--- Aging Information ---")
    show_aging_info(pq)
    
    # Find highest priority job
    print("\n--- Finding Highest Priority Job ---")
    highest_idx = find_highest_priority_job(pq)
    if highest_idx != -1:
        highest_job = pq.queue[highest_idx]
        print(f"Highest priority job: {highest_job.job_id} with priority {highest_job.priority} and waiting time {highest_job.waiting_time:.1f}s")
    
    # Wait a bit more to trigger natural aging
    print("\n--- Waiting 6 more seconds to trigger aging ---")
    time.sleep(6)
    
    # Apply automatic aging
    print("\n--- Applying Automatic Aging ---")
    apply_aging(pq)
    
    # Show status after aging
    update_all_waiting_times(pq)
    pq.show_status()
    
    # Force aging for demonstration
    print("\n--- Force Aging All Jobs ---")
    force_aging(pq)
    
    # Final status
    update_all_waiting_times(pq)
    pq.show_status()
    
    # Final aging info
    show_aging_info(pq)