# Implementing Class Inheritance
# Adding New attributes to the Subclass instances"

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

# if a class itself is an object, that
# means that it has to have it own
# internal dictionary to manage attribute.


print(Employee.__dict__)

e = Employee("Ji-Soo", 38, 1000)
Employee.__dict__["increase_salary"](e, 20)
