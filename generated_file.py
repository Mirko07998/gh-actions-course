import unittest
from io import StringIO
import sys
from hello_world import print_hello_world

class TestHelloWorld(unittest.TestCase):
    def test_print_hello_world(self):
        """Test the output of the print_hello_world function."""
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        print_hello_world()
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()