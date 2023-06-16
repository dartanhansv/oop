# Implementing Class Inheritance

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


class Tester(Employee):  # Inherit methods from the Employee class
    # But it also have its own methods
    def run_tests(self):
        print(f"Testing is started by {self.name}... ")
        print("Tests are done.")


employee1 = Tester("Lauren", 44, 1000)
employee1.increase_salary(20)
print(employee1.salary)

# call the subclass method
employee1.run_tests()

# The Tester subclass has it own method,
# but it also has access to all the
# methods from the Employee Class.

# But if the employee1 instance was instantiated from
# the Employee class, we wouldn't be able to run
# the run_tests method because inheritance doesn't
# work the other way around.

# Tester is a subclass of Employee
# Tester instances can run methods from the Employee class
# Class intances can not run methods from Tester class
