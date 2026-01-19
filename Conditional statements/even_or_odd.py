"""even or odd"""


def even_or_odd(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


number = int(input("Enter the number: "))
even_or_odd(number)
