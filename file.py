# # To open a file
# f = open("file.txt")
# content = f.read()
# print(content)
# f.close()
#
# # 2nd Method
# f = open("file.txt", "r")
# content = f.read(3)
# print(content)
# content = f.read(5)
# print(content)
# f.close()
#
# # Read line
# f = open("file.txt", "r")
# print(f.readline())
# print(f.readlines())
# f.close()
#
# # To write on a file
# f = open("file.txt", "w")
# w = f.write("1.Hello Everyone \n2.This is IT classroom")
# f.close()
#
# # To read and write both
# f = open("file.txt", "r+")
# pri = f.read()
# print(pri)
# z = f.write("\n3.4th Sem \n4.BIT Durg")
# f.close()

# append
with open("file.txt", "a") as file:
    file.write("\nThis is my file1")
    file.write("\nThis is my file2")
