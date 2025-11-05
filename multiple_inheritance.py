class Dad:
    def house(self):
        print("Blue house")
class Mom:
    def shop(self):
        print("orange Color")
class Son(Dad, Mom):
    def factory(self):
        print("White Factory")

son = Son()
son.factory()
son.house()
son.shop()