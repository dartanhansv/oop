# #6 Accessing Class Attribute and Methods"
# Classes are Objects too
# Defining Class attributes

class Employee:
    # a example of Class method
    minimum_wage = 1000

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        # call the Class method directly
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is ${Employee.minimum_wage}')
        self._salary = salary


e = Employee("Ji-Soo", 38, 1000)
Employee.__dict__["increase_salary"](e, 20)
print(e.salary)
