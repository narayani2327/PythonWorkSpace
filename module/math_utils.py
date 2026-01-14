"""
Utility functions for basic math operations and greetings.
"""


def square(num):
    """
    Return the square of a number.

    Args:
        num (int | float): Number to be squared

    Returns:
        int | float: Square of the number
    """
    return num * num


def cube(num):
    """
    Return the cube of a number.

    Args:
        num (int | float): Number to be cubed

    Returns:
        int | float: Cube of the number
    """
    return num * num * num


def greet(name):
    """
    Print a greeting message.

    Args:
        name (str): Name of the person
    """
    print(f"Hello {name}")
