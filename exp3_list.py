# Create a list and perform the following methods:
# 1.insert('@')    2.remove(index-2)    3.append(100)    4.length    5.pop()    6.clear

list1 = [1, 2, "a", "b", "c", 50, "+", "BIT", "IT"]
print(list1)

# inserting "@"
list1.insert(0, "@")
print(list1)

# removing element at index 2
del list1[2]
print(list1)

# appending 100
list1.append(100)
print(list1)

# length
length = len(list1)
print("Length of list is", length)

# Applying pop() operation
list1.pop()
print(list1)


# clearing list
list1.clear()
print(list1)