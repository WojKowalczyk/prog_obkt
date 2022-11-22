class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)


class NazwanyPunkt(Punkt):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        super().__init__(nazwa)


