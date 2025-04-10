import unittest
import calc

class TestCalc(unittest.TestCase): # pick any name you want for this class. it inherits from the unittest.TestCase class.
    def test_add(self): # all methods from the TestCalc class must start with "test_" so that they run properly
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()