"""Demonstration of abstraction using a Vehicle abstract base class."""


from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class representing a vehicle."""

    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):
        """Drive the vehicle."""
        pass


class PetrolCar(Vehicle):
    """Concrete implementation of a petrol-powered car."""

    def drive(self):
        """Drive using fuel."""
        print(f"{self.brand} is burning fuel to move.")


class ElectricCar(Vehicle):
    """Concrete implementation of an electric-powered car."""

    def drive(self):
        """Drive using battery power."""
        print(f"{self.brand} is using battery power to move.")


def main():
    """Create vehicles and demonstrate abstraction."""
    my_petrol = PetrolCar("Toyota")
    my_petrol.drive()
    # try_vehicle = Vehicle("Generic")
    # ^ This would throw an ERROR: "Can't instantiate abstract class Vehicle"


if __name__ == "__main__":
    main()
