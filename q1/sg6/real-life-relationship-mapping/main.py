# Write a short Python code snippet showing a Course adding a Student object to a list. 

class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

student1 = Student("Amara")
student2 = Student("Xadri")

course = Course("Computer Science")

course.add_student(student1)
course.add_student(student2)

print(course.name)
for student in course.students:
    print(student.name)
