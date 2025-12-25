import unittest
from queue import Queue
from task_1.src.application_manager import generate_request, process_request


class ApplicationManager(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_generate_request(self):
        params = "Test Application"
        generate_request(self.queue, params)
        self.assertFalse(self.queue.empty())
        application = self.queue.get()
        self.assertEqual(application.data, params)

    def test_process_request(self):
        params = "Test Application"
        generate_request(self.queue, params)
        self.assertFalse(self.queue.empty())
        process_request(self.queue)
        self.assertTrue(self.queue.empty())
