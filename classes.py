# First version:
# This is a small and simple example,
# that wouldn't escalate well enough for big applications.
#
# employee1 = ["Ji-Soo", 38, "developer", 1200]
# employee2 = ["Lauren", 44, "tester", 1000]
# employees = [employee1, employee2]
#
# for e in employees:
#    print(f"{e[0]}s' salary is ${e[3]}")


# 2nd version -  with Dictionaries
# Now we do not need to remember which index
# is used for which piece of data.
# I can refer to the data by name

employee1 = {
    "name": "Ji-Soo",
    "age": 38,
    "position": "developer",
    "salary": 1200
    }

employee2 = {"name": "Lauren", "age": 44, "position": "tester", "salary": 1000}


def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent/100)


def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a \
{employee['position']} with the salary of ${employee['salary']} ")


employees = [employee1, employee2]

increase_salary(employee2, 20)
for e in employees:
    employee_info(e)
