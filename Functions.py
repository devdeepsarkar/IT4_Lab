# Builtin Function
a = 9
b = 10
c = sum((a, b))
print(c)


# User defined function
def my_function():      # function definition
    print("Hello from a function")


my_function()           # function calling


def algo_function():
    print("Step 1.1")
    print("Step 2.2")
    print("Step 3")
    print("Step 4")


algo_function()
algo_function()

# print("Step 1.1")
# print("Step 2")
# print("Step 3")
# print("Step 4")
# print("Step 1")
# print("Step 2")
# print("Step 3")
# print("Step 4")


# Accept values in function through arguments or parameters
def my_fun(fname):
    print("Welcome " + fname)


my_fun("abc")
my_fun("Hello")
my_fun("101")


def my_add(q, w):
    print("Addition of", q, "and", w, "is", q + w)


my_add(4, 5)


# If the number of arguments is not known
def my_fun2(*kids):
    print("The youngest child is " + kids[2])


my_fun2("RAJ", "RAM", "SAURABH")


# Default parameter value
def my_fun3(city="Bhilai"):
    print("City is " + city)


my_fun3()
my_fun3("Raipur")


# Passing a list as an arguments
def my_fun4(food):
    for x in food:
        print(x)


fruits = ["Mango", "Banana", "Kiwi"]
my_fun4(fruits)


# Return values
def my_fun5(x):
    return 5 * x


print(my_fun5(9))


# To pass function
def my_fun6():
    pass


my_fun6()

# Recursion
