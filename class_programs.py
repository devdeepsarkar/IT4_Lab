# a) Create a class Employee with attributes employee_name, employee_id and employee_salary.
#    Create two objects employee1 and employee2.

class Employee:
    employee_id = 321
    employee_name = "Devdeep"
    employee_salary = 50000


# Creating objects of class Employee
employee1 = Employee()
employee2 = Employee()
print(employee1.employee_id, employee1.employee_name, employee1.employee_salary)
print(employee2.employee_id, employee2.employee_name, employee2.employee_salary)

# Changing attributes values
employee2.employee_id = 741
employee2.employee_name = "Saurabh"
employee2.employee_salary = 360000
print(employee2.employee_id, employee2.employee_name, employee2.employee_salary)


# b) Create a class Room with attributes length, breadth, initialize with user input. Calculate area of the Room.
class Room:
    length = float(input("Enter Length: "))
    breadth = float(input("Enter breadth: "))

    def area(self):
        area = self.length * self.breadth
        print(f"area = {area}")


room1 = Room()
room1.area()
