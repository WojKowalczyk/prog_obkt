class Student():
    def __init__(self, a = "a"):
        self.a = a


ktos = Student()
ktos.b = "b"
print(ktos.b)
print(ktos.a)