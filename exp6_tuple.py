# Create a tuple and perform the following methods and operations:
# 1.Add items 2.length 3.check for item in tuple 4.Access item

# Creating a tuple
tpl = ("Apple", "Banana", "Cherry", "Orange")
print(tpl)

# Add items in tuple
# tpl[4] = "Kiwi" -- Error: Item Assignment Error
tpl2 = ("Kiwi", "Mango")
tpl = tpl + tpl2
print(tpl)

# Length of tuple
print(len(tpl))

# Check for item in tuple
ck = input("Enter item to check: ")
if ck in tpl:
    print("Yes, " + ck + " is present in tuple")
else:
    print("No, " + ck + " is not present in tuple")

# Access items from a tuple
print(tpl[0])
print(tpl[2:4])
