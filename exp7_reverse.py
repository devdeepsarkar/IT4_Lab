# Write a python program to find reverse of an array using 4 different methods.

# 1. Reverse using slicing method
my_array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Array:", my_array)
my_array = my_array[::-1]
print("Reversed array:", my_array)

# 2. By using reverse()
my_array = [11, 21, 31, 41, 51, 61, 71, 81, 91]
print("Array:", my_array)
my_array.reverse()
print("Reversed array:", my_array)

# 3. By using reversed()
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Array:", my_array)
result = list(reversed(my_array))
print("Reversed array:", result)


# 4.a. Using functions
# def swap_rev():
#     front = 0
#     end = -1
#     for x in range(int(n/2)):
#         temp = my_array[front]
#         my_array[front] = my_array[end]
#         my_array[end] = temp
#         front += 1
#         end -= 1
#
#
# n = int(input("Enter number of elements: "))
# my_array = []
# print("Enter elements: ")
# for i in range(n):
#     my_array.append(int(input("")))
#
# print("Array: ", my_array)
# swap_rev()
# print("Reversed array: ", my_array)

# 4.b. By using loop
my_array = [51, 52, 53, 54, 55, 56, 57, 58, 59]
print("Array:", my_array)
print("Reversed array: ", end="")
for x in range(len(my_array)-1, -1, -1):
    print(my_array[x], end=" ")

