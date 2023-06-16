# Implementing Class Inheritance

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


class Tester(Employee):  # Inherit methods from the Employee class
    pass


employee1 = Tester("Lauren", 44, 1000)
employee1.increase_salary(20)
print(employee1.salary)
