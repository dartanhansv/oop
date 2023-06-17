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


# To validate Class Inheritance
# Create a new Tester instance with the Tester Class
employee1 = Tester("Lauren", 44, 1000)

# Increase the salary of the Tester instance using the
# increase_salary function/method of the Employee Class

employee1.increase_salary(20)

# Print the new salary
print(employee1.salary)
