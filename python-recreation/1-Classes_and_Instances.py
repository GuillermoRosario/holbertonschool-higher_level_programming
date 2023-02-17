#This is an Exercises that Helps develop classes and instances Domination
"""Employee Class Blueprint"""
class Employee:

    """Init method of Employee"""
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gartmediaproductions.com'

    def fullname(self):
        """Full name method to make it easy to print fullname"""
        #We Create methods/functions to faccilitate the calling of complex procedures applying code reuse.
        return (f'{self.first} {self.last}')
    
    def pay_and_email(self):
        """Method to print name and email."""
        return (f'{self.email} {self.pay}')

"""Instances of the Employee Class"""
emp_1 = Employee('Raul', 'Gonzales', 1000)
emp_2 = Employee('Test', 'User', 2500)

print(Employee.fullname(emp_1))
print(emp_1.pay_and_email())