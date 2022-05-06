import unittest
from solution import say_hello

# These example test cases are editable, feel free to add
# your own tests to debug your code.

class Test(unittest.TestCase):
    def test_should_say_hello(self):
        self.assertEqual(say_hello("Qualified"), "Hello, Qualified!")

