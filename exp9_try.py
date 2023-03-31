# Demonstrate a python code to print try, except, else, finally block statement.
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print("Your answer is:", result)
    finally:
        print("This is always executed")


div(10, 0)
div(20, 2)


