# 7.. Using Data Classes
# 7.1. Introducing Data Classes

class Project:
    def __init__(self, name, payment, client):
        self.name = name
        self.payment = payment
        self.client = client

    def __str__(self):
        return (
            f"Project(name={repr(self.name)},"
            f"payment={repr(self.payment)},"
            f"client={repr(self.client)})"
        )


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.salary = project


p = Project("Django App", 2000, "Globomantics")
