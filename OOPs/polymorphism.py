"""Demonstration of polymorphism using vehicle classes."""


class Car:
    """Base class representing a car."""

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        """Drive a standard car."""
        print(f"{self.brand}: Vroom vroom! (Engine roaring)")


class ElectricCar(Car):
    """Electric car with overridden drive behavior."""

    def drive(self):
        """Drive an electric car."""
        print(f"{self.brand}: ... (Silent electric hum)")


class Truck(Car):
    """Truck with overridden drive behavior."""

    def drive(self):
        """Drive a truck."""
        print(f"{self.brand}: Rumble rumble! (Heavy diesel engine)")


def main():
    """Create vehicles and demonstrate polymorphism."""
    garage = [
        Car("Toyota"),
        ElectricCar("Tesla"),
        Truck("Ford"),
    ]

    for vehicle in garage:
        vehicle.drive()


if __name__ == "__main__":
    main()
