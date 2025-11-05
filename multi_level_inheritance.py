class Grandfather:
    def car(self):
        print("Red car")
class Dad(Grandfather):
    def house(self):
        print("Blue house")
class Son(Dad):
    def factory(self):
        print("White Factory")

s = Son()
d = Dad()
g = Grandfather()

g.car()
d.house()
d.car()
s.factory()
s.car()
s.house()