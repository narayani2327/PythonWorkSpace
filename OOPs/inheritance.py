"""Phone and TouchScreen class example."""


class Phone:
    """Represents a basic phone."""

    def __init__(self, storage, ram):
        self.storage = storage
        self.ram = ram

    def show_details(self):
        """Return phone details."""
        return f"Storage: {self.storage}, RAM: {self.ram}"


class TouchScreen(Phone):
    """Represents a touchscreen phone."""

    def __init__(self, storage, ram, touch_type):
        super().__init__(storage, ram)
        self.touch_type = touch_type

    def call(self):
        """Make a call."""
        print("Making a call using touchscreen phone")


if __name__ == "__main__":
    phone_obj = Phone("128GB", "8GB")
    print(phone_obj.show_details())

    touch_phone = TouchScreen("256GB", "12GB", "Capacitive")
    print(touch_phone.show_details())
    touch_phone.call()
