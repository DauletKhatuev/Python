class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}")

teacher1 = Teacher("Bob", "Mathematics")
teacher1.introduce()

student1 = Student("Tom", 2)
student1.introduce()