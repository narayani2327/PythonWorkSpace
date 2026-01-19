"""Employee class example."""


class Employee:
    """Represents an employee with name, ID, and salary."""

    def __new__(cls, *args, **kwargs):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name, employee_id, salary):
        """Initialize an Employee instance."""
        print("Initializing object")
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        """Return employee ID."""
        return self.__employee_id

    def display_details(self):
        """Display employee details."""
        print(f"Name: {self.__name}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: {self.__salary}")


class Manager(Employee):
    """Represents a manager, derived from Employee."""

    def __init__(self, name, employee_id, salary, number_of_projects):
        """Initialize a Manager instance."""
        super().__init__(name, employee_id, salary)
        self.number_of_projects = number_of_projects

    def display_details(self):
        """Display manager details."""
        super().display_details()
        print(f"Number of Projects: {self.number_of_projects}")


def main():
    """Create Employee and Manager instances."""
    employee1 = Employee("Narayani", 123, 1233)
    employee2 = Employee("Kalavathi", 164, 9087)
    employee3 = Employee("Hari", 78, 98)

    employees = {
        employee1.get_employee_id(): employee1,
        employee2.get_employee_id(): employee2,
        employee3.get_employee_id(): employee3,
    }

    for employee in employees.values():
        print("____Employee Details____")
        employee.display_details()

    for i in range(1, 10):
        print(i)

    employee4 = Employee("Kavya", 200, 89937)

    if employee4.get_employee_id() not in employees:
        employees[employee4.get_employee_id()] = employee4
    else:
        print("Employee ID exists")

    for employee in employees.values():
        print("____Employee Details____")
        employee.display_details()

    print("_________________")
    manager = Manager("Anita", 300, 120000, 30)
    manager.display_details()


if __name__ == "__main__":
    main()
