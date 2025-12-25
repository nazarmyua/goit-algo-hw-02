import unittest
from task_2.src.main import is_palindrome


class Palindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
