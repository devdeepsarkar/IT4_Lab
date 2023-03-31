try:
    f = open("Exp.txt")
except Exception as e:
    print(e)
else:
    print("This is my file")
finally:
    print("print the output")
