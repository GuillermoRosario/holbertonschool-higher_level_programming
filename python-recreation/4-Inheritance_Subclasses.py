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
    """Creation of Employee Class Method"""

class Developer(Employee):
    raise_amount = 1.50

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

class Manager(Employee):
    """Inherited class from employee with aditional class methods."""
    #Inheritance adheres the previosuly created class attributes and decaations.
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = []
        else:
            self.employees = employees

def add_emp(self, emp):
    if emp not in self.employees:
        self.employees.remove(emp)

def print(self):
    for emp in self.employees:
        print('-->', emp.fullname())


dev_1 = Developer('Guillermo', 'Rosario', 50000, 'Python')
dev_2 = Developer('Liz','Garcia', 10000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(dev_1.fullname())
print(dev_1.prog_language)
print(dev_1.pay_and_email())