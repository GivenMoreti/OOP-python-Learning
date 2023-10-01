# simple class
class Student:
    name = ""
    grade = ""
    gender = ""

    principal = "sturgis"
    # constructor

    def __init__(self, name, grade, gender):
        self.name = name
        self.grade = grade
        self.gender = gender

    # method 1
    def is_registered(self):
        print(f" {self.name} is registered")

    # object
student_1 = Student("Mike", 12, "male")
print(student_1.is_registered())
print(student_1.principal)
