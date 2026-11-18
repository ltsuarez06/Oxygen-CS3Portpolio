class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = []

        def enroll(self, course):
            self.course.append(course)

        student1 = student("John", 15)
        student2 = student("Jane", 16)
        student3 = student("Mike", 14)

        student1.enroll("Algebra")
        student2.enroll("Geometry")
        student3.enroll("Calculus")

        class teacher:
            def __init__(self, name, subject):
                self.name = name
                self.subject = subject
                self.student =  []

                teacher1 = teacher("Mr. Smith", "Math")
                teacher1.add_student(student1)
                teacher1.add_student(student2)
                teacher1.add_student(student3)

                def add_student(self, student):
                    self.student.append(student)

                    for student in teacher1.student:
                        print(student.name)

                        class course:
                            def __init__(self, name, teacher):
                                self.name = name
                                self.teacher = teacher
                                self.student = []

                                course1 = course("Algebra", teacher1)
                                print(course1.name)
                                print(course1.teacher.name)

                                class person:
                                    def __init__(self, name):
                                        self.name = name

                                        def introduce(self):
                                            print(f"Hello, my name is {self.name}.")

                                        class teacher(person):
                                            def __init__(self, name, subject):
                                                super().__init__(name)
                                                self.subject = subject

                                                def teach(self):
                                                    print(f"Hello, my name is {self.name} and I teach {self.subject}.")

                                                    teacher1 = teacher("Mr. Smith", "Math")
                                                    print(teacher1.name)
                                                    print(teacher1.subject)

                                                class student(person):
                                                    def __init__(self, name, age):
                                                        super().__init__(name)
                                                        self.age = age

                                                        def introduce(self):
                                                            print(f"Hello, my name is {self.name} and I am {self.age} years old.")

                                                            class board:
                                                                def __init__(self, color):
                                                                    self.color = color

                                                                    class classroom:
                                                                        def __init__(self):
                                                                            self.board = board("white")

                                                                            classroom1 = classroom()
                                                                            print(classroom1.board.color)

                                                                            room1 = classroom()
                                                                            print(room1.board.color)

                                                                            class laptop:
                                                                                def __init__(self,brand):
                                                                                    self.brand = brand

                                                                                    laptop1 = laptop("Dell")

                                                                                    class lab:
                                                                                        def __init__(self, laptop):
                                                                                            self.laptop = laptop

                                                                                            lab1 = lab(laptop1)
                                                                                            print(lab1.laptop.brand)

                                                                                            class thermometer:
                                                                                                def __init__(self):
                                                                                                    print("Temperature Measured")

                                                                                                    class scientist:
                                                                                                        def conduct_experiment(self, thermometer):
                                                                                                            thermometer.measure()

                                                                                                            scientist1 = scientist()
                                                                                                            thermometer1 = thermometer()

                                                                                                            scientist1.conduct_experiment(thermometer1)

                                                                                                            

                                                                                            
                                                                        