class Employee:
    """Class representation for employee data"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        return self.tasks.append(task)

class Recruiter(Employee):
    def recruit(self):
        self.add_work("Recruit")

class Developer(Employee):
    def code(self):
        self.add_work("Code")

class Manager(Employee):
    def manage(self):
        self.add_work("Manage")

employee1 = Recruiter("Richard", "1234")
employee2 = Developer("Jelly", "9876")
employee3 = Manager("Charlie", "8193")

employee1.recruit()
employee2.code()
employee3.manage()



