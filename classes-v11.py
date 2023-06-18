# Implementing Class Inheritance
# Extending Parent Class Instance methods with super

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
    # Define the same method present in the Employee Class
    # Than repeat the same calculation. This is hard
    # to mantain.
    # def increase_salary(self, percent, bonus=0):
    #     self.salary += self.salary * (percent/100)
    #     self.salary += bonus

    # So how to access the method from the parent Class?
    # Using the super fuction!
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)  # What happens in the background is:
        # Employee.increase_salary(self,percent) but it wouldn't like
        # if the code was like that because self would refer to the
        # increase_salary of the Developer Class, not from Employee
        # as intended
        self.salary += bonus

    # This is a "DRY" code
    " DRY = Don't Repeat yourself"


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000)


employee1.increase_salary(20)
employee2.increase_salary(20, 30)
print(employee1.salary)
print(employee2.salary)
