"""Exception handling"""


try:
    num = int(input("Enter number: "))
    print("Phase1 completed")
    print(10 / num)
    print("Phase2 completed")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")
