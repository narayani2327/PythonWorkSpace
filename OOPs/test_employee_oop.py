"""Employee class example."""


class Employee:
    """Represents an employee with name, ID, and salary."""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary


def main():
    """Create an Employee instance and print its details."""
    emp1 = Employee("Narayani", 123, 1233)

    print(emp1.name)
    print(emp1.employee_id)
    print(emp1.salary)


if __name__ == "__main__":
    main()
