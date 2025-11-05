class dad: #Parent
    def house(self):
        print("I am from dad class")
class son(dad): #Child
    def factory(self):
        print("I am from son class")

dad = dad()
son = son()
son.house()
son.factory()