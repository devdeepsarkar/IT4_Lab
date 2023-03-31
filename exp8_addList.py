# Write a python function that takes two lists and returns addition of the two list elements
def add_lst(lst1, lst2):
    for x in range(len(lst1)):
        add.append(lst1[x] + lst2[x])


list1 = []
list2 = []
add = []

n = int(input("Enter number of elements: "))

print("Enter elements of list 1 : ")
for i in range(n):
    list1.append(int(input()))

print("Enter elements of list 2 : ")
for i in range(n):
    list2.append(int(input()))

print("list 1:", list1)
print("list 2:", list2)
add_lst(list1, list2)
print("Addition of list 1 and 2:", add)
