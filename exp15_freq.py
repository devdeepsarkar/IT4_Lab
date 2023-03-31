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
