class Student():
    def __init__(self, imie):
        self.imie = imie
    def wartosc(self):
        print(globals())

student_1 = Student("jarek")
student_2 = Student("gawel")

student_1.wartosc()