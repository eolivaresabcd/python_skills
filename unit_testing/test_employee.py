import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase): 
    # careful! tests don't necesarilly run in order, so bear that in mind.
    # this is why we must keep the tests independent of each other.
    # if one test fails, the other tests should still run.

    @classmethod # by using this classmethod decorator, we are telling unittest that this method is a class method.
    # this means that it will be called on the class itself, not on an instance of the class.
    def setUpClass(cls): # these must be camel case
        # This method is called once before all tests
        print('setUpClass')

    @classmethod # by using this classmethod decorator, we are telling unittest that this method is a class method.
    # this means that it will be called on the class itself, not on an instance of the class.
    def tearDownClass(cls): # these must be camel case
        # This method is called once after all tests
        print('tearDownClass')  

    def setUp(self): # these must be camel case
        # This method is called before every test
        print('setUp')
        self.emp1 = Employee('Corey', 'Schafer', 50000) # we must use self. to make it an instance atribute.
        self.emp2 = Employee('Sue', 'Smith', 60000) # we must use self. to make it an instance atribute.
    
    def tearDown(self): # these must be camel case
        # This method is called after every test
        print('tearDown\n')
    # this method is usually used to clean up after the test, but in this case we don't need it.
    # we don't need to clean up anything, because we are not creating any files or database connections.
    # we are just creating instances of the Employee class, and they will be garbage collected after the test.
    # if we are doing ETL to txt files for instance, we would need to clean up the files after the test.
    # this is usually done in the tearDown method, but in this case we don't need it.

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self): 
        #here we are patching the requests.get method, so that we don't have to actually make a request to the webpage.
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True # we are forcing the response to be ok, so that we can test the happy path.
            mocked_get.return_value.text = 'Success' # the response text is what we expect to get from the webpage.

            # once we have mocked the response, we run the method that we want to test.
            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False # we are forcing the response to be not ok, so that we can test the unhappy path.

            # once we have mocked the response, we run the method that we want to test.
            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!') # this string must be the same as the one in the 
                                                        # method that we are testing, so that the test passes.
if __name__ == '__main__':
    unittest.main()