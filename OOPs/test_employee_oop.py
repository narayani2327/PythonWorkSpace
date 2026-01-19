"""Employee class example."""


class Employee:
    """Represents an employee with name, ID, and salary."""

    def __init__(self, name, employee_id, salary):
        """Initialize an Employee instance."""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display employee details."""
        print(self.name)
        print(self.employee_id)
        print(self.salary)


def main():
    """Create an Employee instance and print its details."""
    employee = Employee("Narayani", 123, 1233)
    employee.display_details()


if __name__ == "__main__":
    main()
