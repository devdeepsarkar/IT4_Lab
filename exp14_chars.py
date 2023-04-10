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

# Output:
# Enter the file name: file.txt
# {'T': 4, 'h': 4, 'i': 12, 's': 8, ' ': 12, 'm': 4, 'y': 4, 'f': 4, 'l': 4, 'e': 4, '1': 2, '\n': 3, '2': 2}
# Total chars: 67
