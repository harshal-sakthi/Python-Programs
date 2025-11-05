class Parent:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    def access(self):
        print("Inside Parent Class")
        print("Public: ", self.public_var)
        print("Protected: ", self._protected_var)
        print("Private: ", self.__private_var)

class Child(Parent):
    def access_subclass(self):
        print("Inside Child Class")
        print("Public: ", self.public_var)
        print("Protected: ", self._protected_var)
        try:
            print("Private: ", self.__private_var) #For access this command print("Private: ", self._Parent__private_var)
        except AttributeError:
            print("Private: ❌ Can't Access (AttributeError)")

class Stranger:
    def access_otherclass(self, obj):
        print("Inside Stranger Class")
        print("Public: ", obj.public_var)
        print("Protected: ", obj._protected_var) #⚠️ Not Recommended
        try:
            print("Private: ", obj.__private_var)
        except AttributeError:
            print("Private: ❌ Can't Access (AttributeError)") #for Access print("Private: ", self._Parent__private_var)


p = Parent()
print("\n ➡️ Access fro Same Class :")
p.access()

c = Child()
print("\n ➡️ Access from subclass: ")
c.access_subclass()

s = Stranger()
print("\n ➡️ Access from otherclass: ")
s.access_otherclass(p)