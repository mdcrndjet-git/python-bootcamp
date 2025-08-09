class Person:
    def __init__(self, first_name, last_name):
        self.firs_name =  first_name
        self.last_name = last_name

    def sleep(self):
        print("I will sleep for eight hours")

    def introduce(self):
        print(f"Hello, my name is {self.firs_name} {self.last_name}")

person = Person("John", "Cena")
person.sleep()
person.introduce()