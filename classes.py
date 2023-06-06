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
employees = [employee1, employee2]

for e in employees:
    print(f"{e['name']}s' salary is ${e['salary']}")
