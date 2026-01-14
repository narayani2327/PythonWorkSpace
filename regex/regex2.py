"""
US telephone number validation using regular expressions.
"""

import re


def main():
    """
    Validate a US phone number entered by the user.
    """
    pattern = r"^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$"

    phone = input("Enter US phone number: ")

    if re.fullmatch(pattern, phone):
        print("Valid US phone number")
    else:
        print("Invalid US phone number")


if __name__ == "__main__":
    main()
