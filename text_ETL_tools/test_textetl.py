import unittest
import os
from textetl import TextETL

class TestTextETL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """This method is called once before all tests."""
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """This method is called once after all tests."""
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.input_file = 'input.txt'
        with open (self.input_file, 'w', encoding='utf-8') as f:
            f.write("Line 1\nLine 2\nLine 3\n")

    def tearDown(self):
        print('tearDown\n')
        # Clean up the input file after each test
        try:
            os.remove(self.input_file)
        except FileNotFoundError:
            pass

    def test_copy_file(self):
        print('test_copy_file')
        output_file = 'output.txt'
        etl = TextETL(self.input_file, output_file)
        
        # Run the ETL process
        etl.run()
        
        # Check if the output file exists
        self.assertTrue(os.path.exists(output_file))
        
        # Clean up the output file after the test
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()

    