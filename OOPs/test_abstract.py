"""Demonstration of abstraction."""

from abc import ABC, abstractmethod


class Electronics(ABC):
    """Abstract base class for electronic devices."""

    @abstractmethod
    def play_video(self):
        """Play a video."""
        raise NotImplementedError


class Laptop(Electronics):
    """Laptop implementation of Electronics."""

    def play_video(self):
        """Play video using laptop controls."""
        print("Press play button from keypad")


class Mobile(Electronics):
    """Mobile implementation of Electronics."""

    def play_video(self):
        """Play video using mobile screen."""
        print("Press play button on screen")


def main():
    """Demonstrate abstraction."""
    laptop = Laptop()
    laptop.play_video()

    mobile = Mobile()
    mobile.play_video()


if __name__ == "__main__":
    main()
