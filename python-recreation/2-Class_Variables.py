#This is an Exercises that Helps develop classes and instances Domination
"""Employee Class Blueprint"""
class Employee:
    """Class Variable that applies raise amount"""
    #Class Variables are used to define attributes that will be used troughout the program. 
    # We can apply .self individual or ClassName variables that affect the Global Class. 
    num_of_emps = 0
    raise_amount = 1.04

    """Init method of Employee"""
    def __init__(self, first, last, pay):
        """Instance Variables"""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gartmediaproductions.com'

        Employee.num_of_emps += 1

    def fullname(self):
        """Full name method to make it easy to print fullname"""
        #We Create methods/functions to faccilitate the calling of complex procedures applying code reuse.
        return (f'{self.first} {self.last}')
    
    def pay_and_email(self):
        """Method to print name and email."""
        return (f'{self.email} {self.pay}')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

"""Instances of the Employee Class"""
emp_1 = Employee('Raul', 'Gonzales', 1000)
emp_2 = Employee('Test', 'User', 2500)

print(Employee.num_of_emps)
