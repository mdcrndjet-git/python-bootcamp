class Employee:
    """Class representation for employee data"""

    """Class constructor/initialization"""
    def __init__(self,name, id):
        print(f"Employee {name} object created/initialized with ID {id}.")


employee_1 = Employee("Richard","123")
employee_2 = Employee("Jelly","456")

print(employee_1)
print(employee_2)