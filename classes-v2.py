# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary


# employee1 = Employee("Ji-Soo", 38, "developer", 1200)
# employee2 = Employee("Lauren", 44, "tester", 1000)

# print(employee1.name)
# print(employee2.name)

class Employee:
    def __init__(self):
        self.name = "Ji-Soo"
        self.age = 38
        self.position = "developer"
        self.salary = 1200


e = Employee()
print(e.name)