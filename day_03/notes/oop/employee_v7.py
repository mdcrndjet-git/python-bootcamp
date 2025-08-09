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

    def add_work(self, tasks):
        self.tasks.append(tasks)

class Manager(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)

    def manage(self):
        self.add_work("Manage")

    def show(self):
        print(self.tasks)

class Recruiter(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)

    def recruit(self):
        self.add_work("Recruit")

class Developer(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)

    def code(self):
        self.add_work("Code")
"""
employee_1 = Employee("Richard","123")
employee_2 = Employee("Jelly","456")

print(employee_1)
print(employee_2)

print("Employee 1 Name:",employee_1.name)
print("Employee 2 Name:",employee_2.name)

employee_1.add_tasks("Task 1")
print("Employee 1 Tasks:",employee_1.tasks)
"""

manager_1 = Manager("John","123")
manager_1.manage()
manager_1.show()
