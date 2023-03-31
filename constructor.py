# class Employee:
#     n = 100
#
#     # constructor
#     def __init__(self, aname, asalary, apos):
#         self.name = aname
#         self.salary = asalary
#         self.pos = apos
#
#     # method
#     def display(self):
#         print(f"The name is: {self.name}, The salary is: {self.salary}, The position is: {self.pos}")
#
#
# emp1 = Employee("Raj", 200000, "HR")  # Constructor
# emp2 = Employee("Arjun", 20000, "Operator")
# emp1.display()  # method calling
# emp2.display()

# class Employee:
#     no_of_employee = 100
#
#
# r = Employee()
# # r.no_of_employee = 500
# Employee.no_of_employee = 300
# print(Employee.no_of_employee)

# decorator
class Employee:
    no_of_employee = 100

    @classmethod  # decorator
    def change_no(cls, newemp):
        cls.no_of_employee = newemp


r = Employee()
r.change_no(150)
print(Employee.no_of_employee)

