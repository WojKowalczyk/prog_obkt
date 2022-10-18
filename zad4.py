class Car():
    def __init__(self, wydajnosc_paliwowa, maks_paliwo, paliwo = 0):
        self.wydajnosc_paliwowa = wydajnosc_paliwowa
        self.maks_paliwo = maks_paliwo
        self.paliwo = paliwo
    def add_fuel(self, litry):
        if(self.paliwo + litry) > self.maks_paliwo:
            return 0
        else:
            self.paliwo = self.paliwo + litry
    def get_fuel_level(self):
        print(str(self.paliwo))
    def drive(self, metry):
        ile_zuzylo = (metry / 1000) * self.wydajnosc_paliwowa
        self.paliwo = self.paliwo - ile_zuzylo


def main():
    samochod = Car(20, 40)
    samochod.add_fuel(30) # zatankuj co najwyzej 30 litrow
    samochod.get_fuel_level() # ile paliwa
    samochod.drive(100) # przejedz 100 metrow
    samochod.get_fuel_level() # ile paliwa zostalo


if __name__=="__main__":
    main()

