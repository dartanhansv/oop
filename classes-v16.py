# 7.. Using Data Classes
# 7.1. Introducing Data Classes

from dataclasses import dataclass


@dataclass  
class Project:
    name: str
    payment: int
    client: str
# Dataclass makes definition of class shorter
# and already has the repr method within


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django App", 2000, "Globomantics")

# Composition:
# Create a new Employee instance using
# the project instance "p" as a parameter:
e = Employee("Ji-Soo", 38, 1200, p)

# validate
print(e.project)
