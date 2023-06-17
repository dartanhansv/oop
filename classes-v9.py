# Implementing Class Inheritance

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}... ")
        print("Tests are done.")


class Developer(Employee):
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000)


employee1.increase_salary(20)
employee2.increase_salary(20, 30)
print(employee1.salary)
print(employee2.salary)


# Methos Overriding
#
# Note that both "Empolyee" and "Developer" classes have
# the "increase_salary" method and the employee2 instance
# choose to use that method from "Developer" class. But why?
#
# The instance will always first look for the method in its
# own class. If the method is there, it will not got search
# for it inside of the superclass.
#
# The method with the same name will always have
# proceedings in the subclass.
