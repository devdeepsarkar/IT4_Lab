# Create a dictionary and apply the following methods :
# 1.print the dictionary 2.access items 3.use get() 4.change values 5.use len

dict1 = {"brand": "Tata",
         "model": "Nexon EV",
         "year": 2021,
         "price": 1700000}

# print the dictionary items
print(dict1)

# Access items
print(dict1["brand"])
print(dict1["model"])
print(dict1["year"])
print(dict1["price"])

# Use get()
X = dict1.get("brand")
print(X)

# Change values
Y = dict1.keys()
print(Y)
dict1["model"] = "Nexon 3.0"
dict1["year"] = 2023
dict1["price"] = 1898542
dict1["type"] = "Electric"
print(dict1)

# Len
print("length =", len(dict1))
