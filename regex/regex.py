"""
Regex expressions example.

Validates whether the input contains only digits.
"""

import re


def main():
    """
    Read user input and validate if it contains only digits.
    """
    text = input("Enter something: ")

    pattern = r"^\d+$"  # Regex pattern for digits only

    if re.match(pattern, text):
        print("Valid input: contains only digits")
    else:
        print("Invalid input: contains letters or symbols")


if __name__ == "__main__":
    main()
