"""
Car class example demonstrating attributes and methods.
"""


class Car:
    """
    Represents a car with brand and color.
    """

    def __init__(self, brand, color):
        """
        Initialize a Car object.

        Args:
            brand (str): Car brand
            color (str): Car color
        """
        self.brand = brand
        self.color = color

    def drive(self):
        """
        Simulate driving the car.
        """
        print(f"This {self.color} {self.brand} is now driving!")


def main():
    """
    Program entry point.
    """
    my_car = Car("Toyota", "Red")

    print(my_car.brand)
    print(my_car.color)

    my_car.drive()


if __name__ == "__main__":
    main()
