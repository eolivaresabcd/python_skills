import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self): # these must be camel case
        # This method is called before every test
        self.emp1 = Employee('Corey', 'Schafer', 50000) # we must use self. to make it an instance atribute.
        self.emp2 = Employee('Sue', 'Smith', 60000) # we must use self. to make it an instance atribute.
    
    def tearDown(self): # these must be camel case
        # This method is called after every test
        return super().tearDown()

    def test_email(self):

        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()s

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

if __name__ == '__main__':
    unittest.main()