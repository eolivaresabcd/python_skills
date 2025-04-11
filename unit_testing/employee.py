import requests

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    # as you can see, this is not a property, but a method
    # because it modifies the state of the object
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        # we make this method so that the tests don't fail if the webpage is down
        # this is a mock of the requests.get method, so that we don't have to actually make a request to the webpage
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad Response!" # this string must be the same as the one in the test, so that the test passes.