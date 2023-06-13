class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        # self.annual_salary = 12 * salary
        # This way, annual salary is always calculated
        self._annual_salary = None  # for caching

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

    # @property
    # def annual_salary(self):
    #     return self.salary * 12
    # # computed property: computation with attributes from the same instance
    # # Now, annual salary is calculated only when we need to access it

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary
    # if annual_salary is None, calculate
    # if not, if annual_salary was already calculated, return its values


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

employee1.salary = 2000
print(employee1.annual_salary)
