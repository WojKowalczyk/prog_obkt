import math

class Circle():
    def __init__(self, promien):
        self.promien = promien
    def pole(self):
        return math.pi * (self.promien**2)
    def obwod(self):
        return math.pi * 2 * self.promien