# 7.. Using Data Classes
# 7.2. Type hinting of instance attributes

from dataclasses import dataclass
from typing import Any


@dataclass
class Project:
    name: str  # Type hints: it is hinting which type of value is expected
    payment: int
    client: Any  # To avoind the need of hinting, you can use Any


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


# Python will not check the type of each attribute.
# We need additional tools to do that, like mypy
# Install: $ python3 -m pip install mypy
# Check:   $ mypy program.py
# Real Example:
# $ mypy classes-v17.py
# classes-v17.py:27: error: Argument 2 to "Project" has incompatible type
# "str"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)

p = Project("Django App", "2000", "Globomantics")
e = Employee("Ji-Soo", 38, 1200, p)
print(e.project)
