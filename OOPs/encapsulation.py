"""Demonstration of encapsulation in a BankAccount class."""


class BankAccount:
    """Represents a bank account with encapsulated balance."""

    def __init__(self, account_number, initial_balance=0, branch_name="Main Branch"):
        self.account_number = account_number  # Public attribute
        self.__balance = initial_balance      # Private attribute
        self._branch_name = branch_name       # Protected attribute

    def get_balance(self):
        """Return the current account balance."""
        return self.__balance

    def set_balance(self, amount):
        """Set account balance if the amount is valid."""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")


if __name__ == "__main__":
    account = BankAccount("123456789", 1000)

    # account.__balance = 5000  # This will not change the actual balance
    account.set_balance(1000)

    print(account.account_number)
    # print(account.__balance)  # This would raise an AttributeError
    print(account.get_balance())
