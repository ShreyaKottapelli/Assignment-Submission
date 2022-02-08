# DAY 4 ASSIGNMENT OF PYTHON
# FACTORIAL OF ANY NUMBER
import math


def fact():
    if num < 0:
        print("Factorial does not exist for negative number")
    elif num == 0:
        print("The factorial of 0 is always 1")
    else:
        factorial = math.factorial(num)
        print("The factorial of", num, "is", factorial)


num = int(input("Enter a number: "))
fact()
