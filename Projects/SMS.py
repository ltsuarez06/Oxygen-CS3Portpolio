class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []  # List to hold courses the student is enrolled in

    def enroll(self, course):
        self.courses.append(course)

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello! My name is", self.name)

class Teacher(Person):
    def __init__(self, name, subject):
        super()._init__(name)
        self.subject = subject
    def teach(self):
        print(self.name, "is teaching.")

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

# Add the Teacher class
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []  # List to hold students assigned to the teacher

    def add_student(self, student):
        self.students.append(student)

math = Course("Mathematics")
science = Course("Science")
physics = Course("Physics")

# Create a student object
student1 = Student("Tsupilo", 9)
student2 = Student("Marquez", 9)
student3 = Student("Jadolah", 9)

student1.enroll(math)
student1.enroll(science)
student1.enroll(physics)
student2.enroll(math)
student3.enroll(science)
student3.enroll(physics)

# Create a teacher object
teacher1 = Teacher("Mr. Nosneb", "Mathematics")
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher1.add_student(student3)
 
Person1 = Person("Mr.Nosneb")
print(Person1.name)
print(Person1.subject)

# Print the information
print(teacher1.name)
print(teacher1.subject)

print(teacher1.students[0].name) #Tsupilo
print(teacher1.students[0].grade) #9

print(teacher1.students[1].name) #Marquez
print(teacher1.students[1].grade) #9

print(teacher1.students[2].name) #Jadolah
print(teacher1.students[2].grade) #9
