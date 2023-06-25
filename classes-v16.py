# 7.. Using Data Classes
# 7.1. Introducing Data Classes

class Project:
    def __init__(self, name, payment, client):
        self.name = name
        self.payment = payment
        self.client = client


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.salary = project
