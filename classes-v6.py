class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.annual_salary = 12 * salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

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

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

    @property
    def annual_salary(self):
        return self.salary * 12
    # computed property: computation with attributes from the same instance


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

employee1.salary = 2000
print(employee1.salary)
