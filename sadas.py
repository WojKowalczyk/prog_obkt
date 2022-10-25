class Wymierna:
    def __init__(self, licznik = 0, mianownik = 1):
        self.licznik = licznik
        self.mianownik = mianownik
        if self.mianownik < 1:
            self.mianownik = 1
            print("q powinno byc dodatnie")
        if self.mianownik == 0:
            print("q nie moze byc 0")
    def get_licznik(self):
        return self.licznik
    def get_mianownik(self):
        return self.mianownik
    def __repr__(self):
        return (str(self.licznik) + "/" + str(self.mianownik))
    def __float__(self):
        return float(self.licznik / self.mianownik)
    def __add__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_c = licznik_a + licznik_b
        else:
            licznik_c = self.licznik + other.licznik
            mianownik_b = other.mianownik
        return Wymierna(licznik_c, mianownik_b)
    def __sub__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_c = licznik_a - licznik_b
        else:
            licznik_c = self.licznik - other.licznik
            mianownik_b = other.mianownik
        return Wymierna(licznik_c, mianownik_b)
    def __eq__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        if (licznik_a >= licznik_b and licznik_b >= licznik_a):
            return True
    def __ne__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        return licznik_a != licznik_b
    def __lt__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        return licznik_a < licznik_b
    def __le__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        return licznik_a <= licznik_b
    def __gt__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        return licznik_a > licznik_b
    def __ge__(self, other):
        if (self.mianownik != other.mianownik):
            mianownik_a = self.mianownik
            mianownik_b = other.mianownik
            licznik_a = self.licznik
            licznik_b = other.licznik
            licznik_b = other.licznik * self.mianownik
            mianownik_a = self.mianownik * other.mianownik
            licznik_a = self.licznik * other.mianownik
            mianownik_b = other.mianownik * self.mianownik
            licznik_a = licznik_a * licznik_b
        else:
            licznik_a = self.licznik
            licznik_b = other.licznik
        return licznik_a >= licznik_b
    def __mul__(self, other):
        licznik_c = self.licznik * other.licznik
        mianownik_c = self.mianownik * other.mianownik
        return Wymierna(licznik_c, mianownik_c)
    def __truediv__(self, other):
        licznik_c = self.licznik * other.mianownik
        mianownik_c = self.mianownik * other.licznik
        return Wymierna(licznik_c, mianownik_c)
def main():
    liczba_a = Wymierna(1, 2)
    liczba_b = Wymierna(1, 3)
    print(Wymierna.get_licznik(liczba_a))
    print(Wymierna.get_mianownik(liczba_a))
    print(str(liczba_a + liczba_b))
    print(str(liczba_a - liczba_b))
    print(str(liczba_a == liczba_b))
    print(str(liczba_a != liczba_b))
    print(str(liczba_a > liczba_b))
    print(str(liczba_a >= liczba_b))
    print(str(liczba_a < liczba_b))
    print(str(liczba_a <= liczba_b))
    print(str(liczba_a * liczba_b))
    print(str(liczba_a / liczba_b))

if __name__ == "__main__":
    main()