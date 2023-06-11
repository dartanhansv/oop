class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

print(employee1.name)
print(employee2.name)

# Terminology
# We could call employee1 and employee2 objects
# but everything is object in Python
# so we call them employee instances
#
# Instantiation
# Is the pocess of using a class
# to create a new object
#
# This code uses the Employee class
# to instantiate new employee instances
