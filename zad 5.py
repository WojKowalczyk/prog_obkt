class Student():
    def __init__(self, imie, nazwisko, wynik_quizow = 0, liczba_quizow = 0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynik_quizow = wynik_quizow
        self.liczba_quizow = liczba_quizow
    def get_name(self):
        print(str(self.imie))
    def get_total_score(self):
        print(str(self.wynik_quizow))
    def add_quiz(self, wynik):
        self.liczba_quizow = self.liczba_quizow + 1
        self.wynik_quizow = self.wynik_quizow + wynik
    def get_average_score(self):
        srednia = self.wynik_quizow / self.liczba_quizow
        print(str(srednia))

def main():
    student_a = Student('jan', 'brzechwa')
    student_a.add_quiz(2)
    student_a.add_quiz(3)
    student_a.add_quiz(4)
    student_a.get_total_score() #wszystkie punkty
    student_a.get_average_score() #srednia


if __name__=="__main__":
    main()
