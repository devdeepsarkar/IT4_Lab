# Short Hand if
a = 50
b = 30
if a > b: print("a is greater than b")

# Short Hand if.. else...
a = 59
b = 44
print("a is greater") if a > b else print("b is greater")

# One line if else statements
a = 330
b = 330
print("a") if a > b else print("=") if a == b else print("b")

# AND
a = 50
b = 30
c = 600
if (a > b) and (c > a):
    print("Both conditions are true")

if (a > b) or (c < a):
    print("At least one of the condition is true")

if not a > c:
    print("a is not greater than c")

# Nested if
x = 5
if x > 10:
    print("Greater than 10")
    if x > 20:
        print("Greater than 20")
else:
    print("Not above 10")

# Pass statement
if a > b:
    pass

