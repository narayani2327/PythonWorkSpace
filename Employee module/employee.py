"""module to calculate salary and leaves"""
from employee_utils import leave_calculator, salary_with_bonus_calculator

name = input("Enter your name: ")
designation = input("Enter your designation: ")
salary = int(input("Enter your salary: "))
leaves = int(input("Enter number of leaves: "))

leaves_detection = leave_calculator(salary, leaves)
salary_with_bonus = salary_with_bonus_calculator(salary, designation)

total_salary = round(salary_with_bonus-leaves_detection)

print(f"{name} with {designation} designation got Rs.{total_salary}")
