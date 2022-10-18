import math


class SodaCan():
    def __init__(self, wysokosc, promien):
        self.wysokosc = wysokosc
        self.promien = promien
    def get_surface_area(self):
        return 2 * math.pi * self.promien * (self.promien + self.wysokosc)
    def get_volume(self):
        return math.pi * (self.promien ** 2) * self.wysokosc

def main():
    puszka = SodaCan(10, 2)
    print(puszka.get_surface_area())
    print(puszka.get_volume())

if __name__ == "__main__":
    main()
