"""module to calculate salary and leaves"""
import logging
from employee_utils import leave_calculator, salary_with_bonus_calculator


logging.basicConfig(level=logging.INFO)

name = input("Enter your name: ")
designation = input("Enter your designation: ")
salary = int(input("Enter your salary: "))
leaves = int(input("Enter number of leaves: "))

logging.info("Leave calculation started")
leaves_detection = leave_calculator(salary, leaves)

logging.info("Salary with bonus calculation started")
salary_with_bonus = salary_with_bonus_calculator(salary, designation)

total_salary = round(salary_with_bonus - leaves_detection)

print(f"{name} with {designation} designation got Rs.{total_salary}")
