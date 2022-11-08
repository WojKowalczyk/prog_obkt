class stringg():
    def __init__(self, slowo = ""):
        self.slowo = slowo
    def get_string(self, ciag):
        self.slowo = ciag
    def print_string(self):
        print(self.slowo.upper())


cos = stringg()
cos.get_string("jozek")
cos.print_string()



