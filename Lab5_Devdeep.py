a = [56, 89, 45, 2, 65, 12, 68, 31, 1]
a.insert(5, 99)  # mutable: list can be changed/modified
print(a)

# Tuple
b = (1, 2, 3, 4, 56) 
print(b)
# b.insert(0, 7)
tp = (1)
print(tp)
tp = (1,)
print(tp)

# to exchange the values
a = 500
b = 610
a, b = b, a
print(a, b)

# for user input
num = int(input("Enter your num: "))
print(num)
name = input("Enter name: ")
print("Name is " + name)

# if_else
var1 = 10
var2 = 20
var3 = 50
if var3 > var2:
    print(var3, "is greater")
if var3 == var2:
    print(var3, "is equal")
else:
    print(var3, "is smaller")

# elif
if var3 > var2:
    print(var3, "is greater")
elif var3 == var2:
    print(var3, "is equal")
else:
    print(var3, "is smaller")
