class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = [] #association

    def add_student(self, student):
        self.students.append(student)

class student:
    def __init__(self, name):
        self.name = name

   