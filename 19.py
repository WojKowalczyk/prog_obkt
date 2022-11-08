class Student():
    def __init__(self, student_name = "jarek"):
        self.student_name = student_name

print(getattr(Student, "self.student_name"))
