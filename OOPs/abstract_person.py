"""Demonstration of abstraction using abstract base classes."""


from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class representing a person."""

    @abstractmethod
    def do_something(self):
        """Perform an action."""
        pass


class Student(Person):
    """Concrete class representing a student."""

    def do_something(self):
        """Student-specific behavior."""
        print("Student is studying.")


class Employee(Person):
    """Concrete class representing an employee."""

    def do_something(self):
        """Employee-specific behavior."""
        print("Employee is working.")


def main():
    """Create objects and demonstrate abstraction."""
    student = Student()
    student.do_something()
    # p1=Person()
    employee = Employee()
    employee.do_something()


if __name__ == "__main__":
    main()
