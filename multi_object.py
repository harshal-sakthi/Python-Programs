class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def display(self):
        print(f"{self.name} in {self.grade} grade")
s1=Student("Harshal","3")
s2=Student("Bhavanisha","1")

s1.display()
s2.display()