# WAP to use split and join methods in the string.
# joint
lst = ["Raj", "Hina", "Leena", "Adi", "Ana"]

for x in lst:
    print(x, "and", end=" ")
print()
srt = " and ".join(lst)
print(srt)

# split
str2 = "Hello welcome to our class"

str3 = str2.split()
print(str3)

str4 = str2.split(" ")
print(str4)

str5 = str2.split(" ", 2)
print(str5)
