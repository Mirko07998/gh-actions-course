import subprocess
import unittest

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        """
        Test to verify that the HelloWorld module prints 'Hello, World!'
        """
        result = subprocess.run(['python3', 'hello_world.py'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()