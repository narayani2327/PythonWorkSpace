"""Demonstration of inheritance and polymorphism using Employee classes."""


class Employee:
    """Base class representing an employee."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        """Return employee salary."""
        return self.salary

    def get_details(self):
        """Return employee details."""
        return f"Employee Name: {self.name}, Salary: {self.get_salary()}"


class Coder(Employee):
    """Employee subclass representing a coder."""

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_salary(self):
        """Return salary including coder bonus."""
        return self.salary + 10_000

    def get_details(self):
        """Return coder details."""
        return (
            f"Employee Name: {self.name}, "
            f"Salary: {self.get_salary()}, "
            f"Programming Language: {self.programming_language}"
        )


class Designer(Employee):
    """Employee subclass representing a designer."""

    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def get_salary(self):
        """Return salary including designer bonus."""
        return self.salary + 5_000

    def get_details(self):
        """Return designer details."""
        return (
            f"Employee Name: {self.name}, "
            f"Salary: {self.get_salary()}, "
            f"Design Tool: {self.design_tool}"
        )


if __name__ == "__main__":
    employees = [
        Employee("Alice", 70_000),
        Coder("Bob", 90_000, "Python"),
        Designer("Charlie", 80_000, "Photoshop"),
    ]

    for emp in employees:
        print(emp.get_details())
