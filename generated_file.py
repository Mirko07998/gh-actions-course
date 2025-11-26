import unittest
from io import StringIO
import sys
from hello_world import print_hello

class TestHelloWorld(unittest.TestCase):
    def test_print_hello(self):
        """
        Test that print_hello() outputs the expected string.
        """
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        print_hello()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if output is as expected
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()