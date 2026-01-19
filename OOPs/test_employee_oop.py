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
    """Create an Employee instance and print its details."""
    employee1 = Employee("Narayani", 123, 1233)
    employee3 = Employee("Hari", 78, 98)
    employee2 = Employee("Kalavathi", 164, 9087)
    employee1.display_details()
    employees = [employee1, employee2, employee3]
    for item in employees:
        print("____Employee Details____")
        item.display_details()
    for i in range(1, 10):
        print(i)
    employee4 = Employee("Kavya", 164, 89937)
    valid = True
    for item in employees:
        if item.employee_id == employee4.employee_id:
            valid = False

    if valid:
        employees.append(employee4)
    else:
        print("Employee ID exists")
    for item in employees:
        print("____Employee Details____")
        item.display_details()


if __name__ == "__main__":
    main()
