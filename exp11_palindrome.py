# WAP code to check whether the given string is palindrome or not.
# a. Number
num = int(input("Enter the number: "))
rev = 0
q = num

while q:
    dig = q % 10
    rev = rev * 10 + dig
    q = q // 10

if rev == num:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

# b. string
srt = input("Enter the string: ")
srt_rev = srt[::-1]

if srt_rev == srt:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
