class Student:
    name = "Devdeep"
    branch = "IT"
    sem = "4th"

    # To create method
    def info(c):
        print(f"{c.name} is a {c.branch} student")

# Create Object of class
a = Student()
b = Student()

# Use class attribute
print(a.name)
print(b.name)
print(a.branch)
print(a.sem)

# To change Value
b.name = "Rahul"
b.branch = "EEE"
b.sem = "6th"
print(b.name, b.branch, b.sem)
print(a.name, a.branch, a.sem)

# calling mathod
c = Student()
c.info()

