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
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


def main():
    """Create Employee instances and manage employees dictionary."""
    employee1 = Employee("Narayani", 123, 1233)
    employee2 = Employee("Kalavathi", 164, 9087)
    employee3 = Employee("Hari", 78, 98)

    employees = {
        "emp1": employee1,
        "emp2": employee2,
        "emp3": employee3,
    }

    for employee in employees.values():
        print("____Employee Details____")
        employee.display_details()

    for i in range(1, 10):
        print(i)

    employee4 = Employee("Kavya", 164, 89937)

    valid = True
    for employee in employees.values():
        if employee.employee_id == employee4.employee_id:
            valid = False
            break

    if valid:
        employees["emp4"] = employee4
    else:
        print("Employee ID exists")

    for employee in employees.values():
        print("____Employee Details____")
        employee.display_details()


if __name__ == "__main__":
    main()
