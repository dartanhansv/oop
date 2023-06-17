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

# Instance returns True if the 1st argument is
# an instance of the class from the 2nd argument

# employee is a Tester instance and it is also
# a instance of Employee as Tester is the
# subclass of Employee
print(isinstance(employee1, Tester))
print(isinstance(employee1, Employee))

# employee is not an instance of Developer,
# so it will return False
print(isinstance(employee1, Developer))
print("\n")

# "issubclass" checks for class inheritance
# issubclass(subclass, master class)
# True = the 1st arg is a subclass of the 2nd arg
print(issubclass(Developer, Employee))
print(issubclass(Tester, Employee))
print(issubclass(Employee, Developer))
print(issubclass(Employee, Tester))
print(issubclass(Developer, object))
print(issubclass(Tester, object))
print(issubclass(Employee, object))

# Developer and Tester are subclasses of Employee
# Employee is not a subclasses of Tester/Developer
# All classes are subclasses of class object
