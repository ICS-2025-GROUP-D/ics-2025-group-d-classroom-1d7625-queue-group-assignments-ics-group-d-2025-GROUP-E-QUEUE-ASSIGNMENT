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

def show_with_update(pq):
    """Helper to update all waiting times and display the queue."""
    update_all_waiting_times(pq)
    pq.show_status()

def main():
    # Create queue and initialize aging configuration
    pq = PrintQueue(3)
    initialize_queue_for_aging(pq, aging_interval=5, aging_increment=1)  # Aging every 5 seconds

    print("=== Basic Queue Operations ===")
    pq.enqueue_job("user1", "job001", 2)
    pq.enqueue_job("user2", "job002", 4)

    print("\n--- Waiting 2 seconds ---")
    time.sleep(2)
    show_with_update(pq)

    # Fill the queue completely
    pq.enqueue_job("user3", "job003", 5)

    print("\n--- Waiting another 3 seconds ---")
    time.sleep(3)

    # Attempt to add one more job (should fail)
    try:
        pq.enqueue_job("user4", "job004", 1)
    except Exception as e:
        print(f"Error: {e}")

    show_with_update(pq)

    print("\n--- Dequeuing one job to make space ---")
    pq.dequeue_job()
    pq.enqueue_job("user4", "job004", 1)

    print("\n=== Advanced Priority Features ===")
    show_with_update(pq)

    print("\n--- Aging Information ---")
    show_aging_info(pq)

    print("\n--- Finding Highest Priority Job ---")
    highest_idx = find_highest_priority_job(pq)
    if highest_idx != -1:
        highest_job = pq.queue[highest_idx]
        print(f"Highest priority job: {highest_job.job_id} "
              f"(Priority: {highest_job.priority}, Waiting Time: {highest_job.waiting_time:.1f}s)")

    print("\n--- Waiting 6 more seconds to trigger aging ---")
    time.sleep(6)

    print("\n--- Applying Automatic Aging ---")
    apply_aging(pq)
    show_with_update(pq)

    print("\n--- Force Aging All Jobs ---")
    force_aging(pq)
    show_with_update(pq)

    print("\n--- Final Aging Info ---")
    show_aging_info(pq)

if __name__ == "__main__":
    main()
