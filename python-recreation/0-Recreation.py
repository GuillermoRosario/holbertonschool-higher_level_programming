#OOP Python

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
n = Person("Guillermo", 10)
print(n.get_name())
a = Person("Guillermo", 10)
print(a.get_age())