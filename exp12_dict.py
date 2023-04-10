# Write a program to count the numbers of characters in the string
# and store them in a dictionary data structure.
dicts = {}
srt = input("Enter string: ").upper()
for x in srt:
    if dicts.get(x):
        dicts[x] = dicts[x] + 1
    else:
        dicts[x] = 1
print(dicts)

# Enter string: Hello This is IT Classroom
# {'H': 2, 'E': 1, 'L': 3, 'O': 3, ' ': 4, 'T': 2, 'I': 3, 'S': 4, 'C': 1, 'A': 1, 'R': 1, 'M': 1}