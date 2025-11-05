from overwrite import Dad


class Son(Dad):
    def factory(self):
        print("white")
    def house(self):
        print("blue")
son = Son()
son.factory()
son.house()