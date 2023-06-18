# Implementing Class Inheritance
# Adding New attributes to the Subclass instances"

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


# This Developer Class inharent methods from the Employee Class
# Meaning that it will create new instances(Developers employees)
# using the attributes defined on the init method of Employee Class
# What if the Subclass need more attributes that the parent class?
class Developer(Employee):
    # Just override the init method, adding the new attribute:
    def __init__(self, name, age, salary, project):
        # And to avoid code repetition - remember DRY -
        # use "super" to invoke the init method from the
        # Employee Class
        super().__init__(name, age, salary)
        self.project = project

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000, "Project ABC")


employee1.increase_salary(20)
employee2.increase_salary(20, 30)
print(employee1.salary)
print(employee2.salary)
