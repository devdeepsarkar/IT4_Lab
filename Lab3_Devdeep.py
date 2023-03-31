# List
a = list(("Hello", "World"))
print(a)

# Tuple
b = tuple((1, 2, 3, 4))
print(b)

# Dictionaries
x = {"Book" : "Intro to Python", "Year" : 2022}
print(dict(x))
y = dict(name="durg", age=20)
print(y)

# Set
thisset = {"Cherry", "Mango", "Apple", 2, 2, 2, "Cherry"}
print(thisset)

# Booleans
print(10 > 9)
print(10 > 9, 10 == 9, 4 < 6)

a = 10
b = 9
if b > a:
    print("b is greater")
else:
    print("a is greater")

# Numbers
x = 35e3
y = 5E4
print(x, y)

# typecasting
x = 10
y = 11.5
z = 5 + 6j
a = float(x)
b = int(y)
print(a, b)

import random
print(random.randrange(1, 10))

