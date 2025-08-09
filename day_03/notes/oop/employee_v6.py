class Employee:
    """Class representation for employee data"""

    """Class constructor/initialization"""
    def __init__(self,name, id):
        self.name = name
        self.id = id
        self.tasks = []

        print(f"Employee {self.name} object created/initialized with ID {self.id}.")

    def add_tasks(self, task):
        print(f"Added task {task} to {self.name}")
        return self.tasks.append(task)

employee_1 = Employee("Richard","123")
employee_2 = Employee("Jelly","456")

print(employee_1)
print(employee_2)

print("Employee 1 Name:",employee_1.name)
print("Employee 2 Name:",employee_2.name)

employee_1.add_tasks("Task 1")
print("Employee 1 Tasks:",employee_1.tasks)