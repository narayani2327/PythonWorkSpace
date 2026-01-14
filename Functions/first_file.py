"""
Program: Student Utility Program
Purpose: Demonstrate how to define and call functions in Python.
"""


def greet_student(name):
    """
    Greet a student by name.

    Args:
        name (str): Student name
    """
    print(f"Hello {name}, welcome to the Python class!")


def greet_someone(name="Narayani"):
    """
    Greet a default student.

    Args:
        name (str): Student name (default is Narayani)
    """
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
    """
    Calculate total marks.

    Args:
        marks (list[int]): List of marks

    Returns:
        int: Total marks
    """
    return sum(marks)


def calculate_average(total, count):
    """
    Calculate average marks.

    Args:
        total (int): Total marks
        count (int): Number of subjects

    Returns:
        float: Average marks
    """
    return total / count


def check_result(average):
    """
    Determine pass or fail based on average marks.

    Args:
        average (float): Average marks

    Returns:
        str: PASS or FAIL
    """
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    """
    Display student results.

    Args:
        name (str): Student name
        marks (list[int]): List of marks
    """
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    greet_someone()
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Result: {result}")


def main():
    """
    Program entry point.
    """
    student_name = "Narayani H"
    student_marks = [97, 96, 99, 100, 95]

    display_result(student_name, student_marks)


if __name__ == "__main__":
    main()
