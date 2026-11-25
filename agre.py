class student:
    def __init__(self, name):
        self.name = name

        class school:
            def __init__(self, name):
                self.name = name
                self.students = [] #list of students

                def add_student(self, student):
                    self.students.append(student)

                    school = school("St. Mary's School")
                    s1 = student("John")
                    s2 = student("Jane")
                    school.add_student(s1)  
                    school.add_student(s2)

                    print(f"School: {school.name}")
                    print(f"List of Students: ")

                    
                    for student in school.students:
                        print(f"{student.name}")
        
                    