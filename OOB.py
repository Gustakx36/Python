class var:
    def __init__(self):
        self.y = int
        self.x = int
        self.res = int
        self.a = str
        self.b = str
        self.res2 = str
        self.c = str


    def num(self, x, y):
        self.x = x
        self.y = y
        self.res = x + y
        return self.res


    def texto(self, a, b):
        self.a = a
        self.b = b
        self.res2 = a + " " + b
        return self .res2

d = var()

print(d.num(1, 2))
print()
print(d.texto("Bom", "Dia"))
