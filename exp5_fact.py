# Write a python program to find factorial of a given number using functions.
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num * factorial(num - 1)
        print(num, fact)
        return fact


x = int(input("Enter any number: "))
print("Factorial of", x, "is", factorial(x))
