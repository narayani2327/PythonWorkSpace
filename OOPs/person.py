"""Demonstration of encapsulation using public, protected, and private attributes."""


class Person:
    """Represents a person with encapsulated attributes."""

    def __init__(self, name, age, twitter_handle="abc"):
        self.name = name
        self.age = age
        self.__twitter_handle = twitter_handle  # Private attribute
        self._password = "default_password"     # Protected attribute

    def get_twitter_handle(self):
        """Return the private Twitter handle."""
        return self.__twitter_handle

    def set_twitter_handle(self, handle):
        """Set a new Twitter handle."""
        self.__twitter_handle = handle

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
