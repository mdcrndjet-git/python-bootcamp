class Employee:
    """Class representation for employee data"""

    """Class constructor/initialization"""
    def __init__(self,name):
        print(f"Employee {name} object created/initialized.")


employee_1 = Employee("Richard")
employee_2 = Employee("Jelly")

print(employee_1)
print(employee_2)