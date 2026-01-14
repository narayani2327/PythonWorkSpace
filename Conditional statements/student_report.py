"""marks with level"""
name = input("Enter your name: ")
marks = int(input("Enter marks: "))
if marks > 70:
    print(f"{name} got Distintion")
elif marks > 60:
    print(f"{name} got First class")
elif marks > 50:
    print(f"{name} got Second class")
else:
    print(f"{name} has failed")
