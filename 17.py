class Student():
    def __init__(self, imie):
        self.imie = imie


ktos = Student("jarek")

print(ktos.__dict__.keys())
print(Student.__module__)