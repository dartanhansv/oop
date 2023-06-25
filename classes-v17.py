# 7.. Using Data Classes
# 7.1. Introducing Data Classes

from dataclasses import dataclass


@dataclass
class Project:
    name: str  # Type hints: it is hinting which type of value is expected
    payment: int
    client: str


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django App", 2000, "Globomantics")
e = Employee("Ji-Soo", 38, 1200, p)
print(e.project)
