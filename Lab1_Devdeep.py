# Creating variable
x = 5
y = "IT Dept"
z = 12.2
print(x, y, z)

# DataType Casting
x = int(12)
print(x)
print(str(y))
print(float(3))

# gettype
var1 = 10
var2 = "hello"
var3 = 10.5
print(type(var1))
print(type(var2))
print(type(var3))

# Single and Double Quotes
str1 = 'SingleQuote'
str2 = "DoubleQuote"
print(str1, str2)

# Case Sensitive
a = 5
A = "Data"
print(a, A)

# Assign Multiple Values
x, y, z = "Hello", "BIT", "Durg"
print(x, y, z)

# One Value to Multiple Variable
x = y = z = "India"
print(x, y, z)

# Global Variable
B = 35
def my_fun():
    print("My age is", B)
my_fun()

C1 = 35
def my_fun():
    c2 = 20
    print(C1 + 10)
    print(c2 + 10)
my_fun()
print(C1 + 2)
