import unittest
from task_3.src.main import is_valid


class Palindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_valid("( ){[ 1 ]( 1 + 3 )( ){ }}"))
        self.assertFalse(is_valid("( 23 ( 2 - 3);"))
        self.assertFalse(is_valid("( 11 }"))
