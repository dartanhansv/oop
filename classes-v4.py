class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    # Fuction defined within classes = Instance fuctions
    # or methods
    def increase_salary(employee, percent):
        employee.salary += employee.salary * (percent/100)

    def __str__(self):
        return (
            f"{self.name} is {self.age} years old."
            f"Employee is a {self.position} with the salary of ${self.salary}"
        )

    def __repr__(self):
        return (
            f"Employee({repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self.salary = salary


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

employee1.set_salary(200)
print(employee1.get_salary())
