class Employee:
    """Class representation for employee data"""

    """Class constructor/initialization"""
    def __init__(self,name, id):
        self.name = name
        self.id = id
        print(f"Employee {self.name} object created/initialized with ID {self.id}.")

employee_1 = Employee("Richard","123")
employee_2 = Employee("Jelly","456")

print(employee_1)
print(employee_2)

print("Employee 1 Name:",employee_1.name)
print("Employee 2 Name:",employee_2.name)