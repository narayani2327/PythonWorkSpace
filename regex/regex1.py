"""
User registration validation using regular expressions.
"""

import re


def validate_user_details(email, mobile, password):
    """
    Validate user email, mobile number, and password.

    Args:
        email (str): User email address
        mobile (str): Indian mobile number
        password (str): User password

    Returns:
        str: Validation success message

    Raises:
        ValueError: If any validation fails
    """
    email_pattern = (
        r"^[a-zA-Z0-9._%+-]+@"
        r"[a-zA-Z0-9.-]+\."
        r"[a-zA-Z]{2,}$"
    )
    mobile_pattern = r"^[6-9]\d{9}$"
    password_pattern = (
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
        r"(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )

    if not re.match(email_pattern, email):
        raise ValueError("Invalid email address")

    if not re.match(mobile_pattern, mobile):
        raise ValueError("Invalid Indian mobile number")

    if not re.match(password_pattern, password):
        raise ValueError("Password must be strong")

    return "All details are valid"


def main():
    """
    Program entry point.
    """
    try:
        print("User Registration Validation")

        email = input("Enter email: ")
        mobile = input("Enter mobile number: ")
        password = input("Enter password: ")

        result = validate_user_details(email, mobile, password)
        print(result)

    except ValueError as error:
        print("Validation Error:", error)

    else:
        print("User registered successfully")

    finally:
        print("\n--- REGISTRATION PROCESS ENDED ---")


if __name__ == "__main__":
    main()
