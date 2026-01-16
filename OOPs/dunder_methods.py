"""
Demonstration of __new__ and __init__ methods.
"""


class Demo:
    """Demo class to show object creation and initialization."""

    def __new__(cls):
        """
        Create a new instance of the class.

        Args:
            cls (type): Class reference

        Returns:
            Demo: New instance of Demo
        """
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        """
        Initialize the instance.
        """
        print("Initializing object")


def main():
    """
    Program entry point.
    """
    _ = Demo()
    print("hello")


if __name__ == "__main__":
    main()
