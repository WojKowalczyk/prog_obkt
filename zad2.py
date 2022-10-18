class Adres:
    def __init__(self, nr_domu, ulica, miasto, kod_pocztowy, nr_mieszkania=""):
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy
        self.nr_mieszkania = nr_mieszkania
    def show(self):
        print(self.ulica + self.nr_domu + self.nr_mieszkania)
        print(self.miasto + self.kod_pocztowy)
    def comes_before(self, other):
        self.kod_pocztowy = self.kod_pocztowy.replace("-", "")
        self.kod_pocztowy = int(self.kod_pocztowy)
        other.kod_pocztowy = other.kod_pocztowy.replace("-", "")
        other.kod_pocztowy = int(other.kod_pocztowy)
        if self.kod_pocztowy > other.kod_pocztowy:
            print("jest przed innym")


def main():
    adres_a = Adres("5", "orzeszkowa", "olsztyn", "00-120")
    adres_b = Adres("6", "orzeszkowalska", "olsztyn", "00-000")
    adres_a.show()
    adres_a.comes_before(adres_b)


if __name__=="__main__":
    main()
