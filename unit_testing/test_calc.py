import unittest
import calc

class TestCalc(unittest.TestCase): # pick any name you want for this class. it inherits from the unittest.TestCase class.
    def test_add(self): # all methods from the TestCalc class must start with "test_" so that they run properly
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1,-1), -2) # added some boundary / problematic conditions
        self.assertEqual(calc.add(-1, 1), 0) # even if we have many methods, all this still counts as a single test.



if __name__ == '__main__':
    unittest.main()

# when running the test script, we get a dot for each successful test and an F for each failed test