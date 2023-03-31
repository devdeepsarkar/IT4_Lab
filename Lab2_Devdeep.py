# DataType
# TextType
x = "hello"
print(type(x))
print(x)

# NumericType
x = 20
y = 2.5
z = 3j
print(type(x), type(y), type(z))
print(x, y, z)

# List
a = [1, 2, 3, 4]
print(type(a))
print(a)

# String
a = "Hello World!"
b = """Good Bye!
Thank You"""
print(a)
print(b)
print(a[11])

# Looping through string
for x in "BANANA":
    print(x)

print(len(b))

# checkstring
txt = "Life is free"
print("free" in txt)
print("Tree" in txt)

if "free" in txt:
    print("free is present")
else:
    print("No free is not present")

# String Slicing
strr = "Hhhello World!"
print(strr[2:10])
print(strr[:10])
print(strr[2:])
print(strr[-5:-1])

print(strr.upper())
print(strr.lower())
s = " Hello World "
print(s.strip())
print(a.replace("l", "a"))
a = "Hello, World, Good Bye"
print(a.split(', '))

# string Concatenation
a = "Hello"
b = "World!"
print(a+" "+b)

age = 10
print(a + " " + str(age))
