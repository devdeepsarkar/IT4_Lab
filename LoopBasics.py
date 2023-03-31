# while Loop
i = 0
while i < 7:
    print(i, end=" ")
    i += 1
    # i = i + 1

# Break Statement
print("\n")
i = 0
while True:
    print(i)
    i += 1
    if i == 3:
        break
# Continue Statement
print("\n")
i = 0
while i < 7:
    i += 1
    print(i)
    if i <= 6:
        continue
    print(i)

# while with else
print("\n")
i = 0
while i < 7:
    print(i)
    i += 1
else:
    print("No longer < 7")

# for loop
fruits = ["apple", "banana", "kiwi", "mango"]
for x in fruits:
    print(x)

# for loop for list of lists
fruits = [["apple", 2], ["banana", 5], ["kiwi", 3], ["mango", 6]]
# for x in fruits:
#     print(x)

# for x, kg in fruits:
#     print(x, kg)

print()
dict1 = dict(fruits)
for x, qty in dict1.items():
    print(x, qty)

# looping through string
for x in "hello":
    print(x)

fruits = ["apple", "banana", "kiwi", "mango"]
for x in fruits:
    print(x)
    if x == "banana":
        break
