a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)
print(a[6])

# list slicing
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(a[4:6])
print(a[:6])
print(a)
print(a[2:])

# Extended Slicing
a = list(range(10, 210, 10))
print(a)
print(a[2:20:3])
print(a[:10:3])

# Sort, reverse, min, max
a = [56, 89, 45, 2, 65, 12, 68, 31, 1]
a.sort()
print(a)
a.reverse()
print(a)
print(len(a))
print(min(a))
print(max(a))

# append
a = [56, 89, 45, 2, 65, 12, 68, 31, 1]
a.append(111)
a.append(61)
print(a)
b = list()
b.append(56)
b.append(23)
b.append(78)
b.append(55)
b.append(34)
b.append(68)
print(b)

# insert
b.insert(0, 6)
b.insert(1, 60)
b.insert(2, 600)
print(b)
b.remove(60)
print(b)
b.pop()
print(b)
print(a, b)
