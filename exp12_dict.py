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