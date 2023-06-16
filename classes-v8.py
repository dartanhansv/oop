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
