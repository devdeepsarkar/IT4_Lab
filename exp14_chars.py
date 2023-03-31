# Write a program to count frequency of characters in a given file.
fname = input("Enter the file name: ")
f = open(fname, "r")
content = f.read()
chars = {}
tchars = 0
for char in content:
    if char in chars:
        chars[char] += 1
        tchars += 1
    else:
        chars[char] = 1
        tchars += 1


print(chars)
print("Total chars:", tchars)
