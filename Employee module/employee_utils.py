"""
Module to calculate employee salary with bonus and leave deductions.
"""


def salary_with_bonus_calculator(salary, designation):
    """
    Calculate salary including bonus based on designation.

    Args:
        salary (float): Base salary of the employee
        designation (str): Employee designation

    Returns:
        float: Salary including bonus
    """
    match designation:
        case "coder":
            return salary + (salary * 10 / 100)
        case "designer":
            return salary + (salary * 15 / 100)
        case "manager":
            return salary + (salary * 5 / 100)
        case _:
            return salary


def leave_calculator(salary, leaves):
    """
    Calculate salary deduction based on excess leaves.

    Args:
        salary (float): Monthly salary
        leaves (int): Number of leaves taken

    Returns:
        float: Salary deduction amount
    """
    if leaves > 15:
        number_of_excess_leaves = leaves - 15
        return (salary / 30) * number_of_excess_leaves

    return 0.0
