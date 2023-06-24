# #6 Accessing Class Attribute and Methods"
# Classes are Objects too
# Defining Class Methods
from datetime import date


class Employee:
    minimum_wage = 1000

    @classmethod
    def change_mininum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):  # dob = date of birth
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day)
                                     < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

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
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is ${Employee.minimum_wage}')
        self._salary = salary


e = Employee("Ji-Soo", 38, 1000)
print(Employee.minimum_wage)
print(e.minimum_wage)
