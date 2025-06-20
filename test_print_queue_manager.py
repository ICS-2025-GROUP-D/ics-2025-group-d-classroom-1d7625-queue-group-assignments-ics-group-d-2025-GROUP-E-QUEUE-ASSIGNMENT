import unittest
from print_queue_manager import PrintQueueManager

class TestCoreQueueManager(unittest.TestCase):

    def test_enqueue(self):
        pq = PrintQueueManager(3)
        result = pq.enqueue_job("U1", "J101", 1)
        self.assertEqual(result, "Job added")
        self.assertEqual(len(pq.get_status()), 1)

    def test_dequeue(self):
        pq = PrintQueueManager(3)
        pq.enqueue_job("U1", "J101", 1)
        job = pq.dequeue_job()
        self.assertEqual(job['job_id'], "J101")
        self.assertEqual(len(pq.get_status()), 0)

    def test_overflow(self):
        pq = PrintQueueManager(2)
        pq.enqueue_job("U1", "J101", 1)
        pq.enqueue_job("U2", "J102", 2)
        result = pq.enqueue_job("U3", "J103", 3)
        self.assertEqual(result, "Queue is full")

    def test_underflow(self):
        pq = PrintQueueManager(2)
        result = pq.dequeue_job()
        self.assertEqual(result, "Queue is empty")

if __name__ == "__main__":
    unittest.main()
