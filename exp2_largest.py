# WAP to find the largest number among three numbers.
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
num3 = float(input("Enter 3rd number:"))
print("Entered numbers:", num1, num2, num3)
if num1 > num2 and num1 > num3:
    # print(num1, "is largest")
    largest = num1
elif num2 > num1 and num2 > num3:
    # print(num2, "is largest")
    largest = num2
else:
    # print(num3, "is largest")
    largest = num3
print("Largest number is ", largest)
