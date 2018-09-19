class Person():
    def __init__(self,name):
        self.name = name   #instance variable

    def getName(self):
        return self.name

    def isEmployee(self):
        return False
    
class Employee(Person):         #inherit to Person

    def isEmployee(self):
        return True


emp = Person("pradip")
print(emp.getName(), emp.isEmployee())
emp = Employee("dipak")
print(emp.getName() , emp.isEmployee())
