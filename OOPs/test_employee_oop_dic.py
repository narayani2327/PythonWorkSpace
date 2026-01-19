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


class Manager(Employee):

    def __init__(self, name, employee_id, salary, number_of_projects):
        """Initialize an Manager instance."""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.number_of_projects = number_of_projects

    def display_details_man(self):
        """Display manager details."""
        print(f"Number of Projects: {self.number_of_projects}")


def main():
    """Create Employee instances and manage employees dictionary."""
    employee1 = Employee("Narayani", 123, 1233)
    employee2 = Employee("Kalavathi", 164, 9087)
    employee3 = Employee("Hari", 78, 98)

    employees = {
        employee1.employee_id: employee1,
        employee2.employee_id: employee2,
        employee3.employee_id: employee3,
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
        employees[employee4.employee_id] = employee4
    else:
        print("Employee ID exists")

    for employee in employees.values():
        print("____Employee Details____")
        employee.display_details()
    man1 = Manager("Kavya", 164, 89937, 30)
    print("_________________")
    man1.display_details()
    man1.display_details_man()


if __name__ == "__main__":
    main()
