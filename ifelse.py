class Student:
    def __init__(self, is_registered, name, course):
        self.is_registered = is_registered
        self.name = name
        self.course = course
    # method to check if registered

    def is_registered(self):
        if Student.is_registered == True:
            print("method success")
        return self.name


# students in the database
students_all = []
student_one = Student(True, "Given", "IT")
student_two = Student(False, "Mike", "Azure")
student_three = Student(True, "test", "test")

# first append all the students in alist for easy manipulation

students_all.append(student_one)
students_all.append(student_two)
students_all.append(student_three)

students_registered = []
# loop through the students_all and append only registered students
for i in students_all:
    if i.is_registered == True:
        students_registered.append(i)
        print(students_registered)

# lets play with registered students list


def func_student(stu): return stu.Student.course


lets_see = filter(func_student, students_registered)
print(lets_see)

# append all registered students in a list
# check if student is registered
# check = lambda reg_stu: reg_stu
# print(Student.is_registered(student_three))
