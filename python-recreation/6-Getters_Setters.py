#This is an Exercises that Helps develop classes and instances Domination
"""Employee Class Blueprint"""
class Employee:
    """Class Variable that applies raise amount"""
    #Class Variables are used to define attributes that will be used troughout the program. 
    # We can apply .self individual or ClassName variables that affect the Global Class. 

    """Init method of Employee"""
    def __init__(self, first, last):
        """Instance Variables"""
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gartmediaproductions.com'
    
    @property
    def fullname(self):
        """Full name method to make it easy to print fullname"""
        #We Create methods/functions to faccilitate the calling of complex procedures applying code reuse.
        return (f'{self.first} {self.last}')
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None
    
    @property
    def email_(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    def pay_and_email(self):
        """Method to print name and email."""
        return (f'{self.email} {self.pay}')


emp_1 = Employee('Guillermo', 'Rosario')


print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email_)
del emp_1.fullname