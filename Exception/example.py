"""
ATM Withdrawal Program.

Demonstrates that the `finally` block ALWAYS executes.
"""

INITIAL_BALANCE = 5000.0


def withdraw_money(balance, amount):
    """
    Withdraw money from the account balance.

    Args:
        balance (float): Current account balance
        amount (float): Amount to withdraw

    Returns:
        float: Remaining balance after withdrawal

    Raises:
        ValueError: If amount is less than or equal to zero
        RuntimeError: If balance is insufficient
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise RuntimeError("Insufficient balance")

    return balance - amount


def main():
    """
    Main program execution.
    """
    balance = INITIAL_BALANCE

    try:
        print("Welcome to the ATM")

        user_input = input("Enter amount to withdraw: ")
        amount = float(user_input)

        balance = withdraw_money(balance, amount)
        print("Withdrawal successful!")
        print(f"Remaining balance: ₹{balance}")

    except ValueError as error:
        print("Input Error:", error)

    except RuntimeError as error:
        print("Transaction Error:", error)

    else:
        print("Transaction completed without errors.")

    finally:
        print("\n--- SESSION CLOSED ---")
        print("Thank you for using the ATM!")


if __name__ == "__main__":
    main()
