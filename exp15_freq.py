# Write a program to compute the number of characters, words and lines in a file.
fname = input("Enter the file name: ")
f = open(fname, "r")
content = f.read()
lines = {}
words = {}
chars = {}

tlines = 0
for line in content.split("\n"):
    if line in lines:
        lines[line] += 1
        tlines += 1
    else:
        lines[line] = 1
        tlines += 1

twords = 0
for word in content.split():
    if word in words:
        words[word] += 1
        twords += 1
    else:
        words[word] = 1
        twords += 1

tchars = 0
for char in content:
    if char in chars:
        chars[char] += 1
        tchars += 1
    else:
        chars[char] = 1
        tchars += 1

print(lines)
print(words)
print(chars)

print("Total lines:", tlines)
print("Total words", twords)
print("Total chars:", tchars)

# Output:
# Enter the file name: file.txt
# {'This is my file1': 2, 'This is my file2': 2}
# {'This': 4, 'is': 4, 'my': 4, 'file1': 2, 'file2': 2}
# {'T': 4, 'h': 4, 'i': 12, 's': 8, ' ': 12, 'm': 4, 'y': 4, 'f': 4, 'l': 4, 'e': 4, '1': 2, '\n': 3, '2': 2}
# Total lines: 4
# Total words 16
# Total chars: 67
