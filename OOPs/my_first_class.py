"""
Class definition example.
"""


class Phone:
    """
    Represents a phone.
    """

    def show_details(self):
        """
        Return details of the phone.

        Returns:
            str: Phone details
        """
        return "Details of phone"


def main():
    """
    Program entry point.
    """
    phone_instance = Phone()
    print(phone_instance.show_details())


if __name__ == "__main__":
    main()
