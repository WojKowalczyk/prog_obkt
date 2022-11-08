class Shape():
    def __init__(self):
        self
    def area(self):
        print("0")


class Square(Shape):
    def __init__(self, dlugosc):
        self.dlugosc = dlugosc
    def area(self, dlugosc):
        print(str(dlugosc**2))
    super().__init__(dlugosc)