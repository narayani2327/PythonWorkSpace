"""Demonstration of multiple inheritance in Python."""


class Calling:
    """Provides calling functionality."""

    def feature1(self):
        """Display calling feature."""
        print("Calling feature")


class Camera:
    """Provides camera functionality."""

    def feature2(self):
        """Display camera feature."""
        print("Camera feature")


class Smartphone(Calling, Camera):
    """Smartphone class inheriting calling and camera features."""

    def explore(self):
        """Explore smartphone features."""
        print("Exploring features of smartphone")


if __name__ == "__main__":
    phone = Smartphone()
    phone.feature1()
    phone.feature2()
    phone.explore()
