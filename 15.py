class Student():
    def __init__(self, nazwa_ucznia, klasa_ucznia, student_id):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id


ktos = Student("jaarek", "2b", "22234")
print(ktos.nazwa_ucznia)