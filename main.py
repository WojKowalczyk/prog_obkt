import math


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def main():
    punkt_a = Punkt(0, 2)
    punkt_b = Punkt(0, 3)
    print(Punkt.distance(p1, p2))


if __name__=="__main__":
    main()