class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(employee, percent):
        employee['salary'] += employee['salary'] * (percent/100)


    def employee_info(employee):
        print(f"{employee['name']} is {employee['age']} years old. Employee is a \
    {employee['position']} with the salary of ${employee['salary']} ")



employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

Employee.employee_info(employee2.__dict__)
Employee.increase_salary(employee2.__dict__, 20)
Employee.employee_info(employee2.__dict__)
