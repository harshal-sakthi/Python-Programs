class MyClass:
     def instance(self):
         print("Instance")
     @classmethod
     def class_method(cls):
         print("Class")
     @staticmethod
     def static_method():
         print("Static")

obj = MyClass()
obj.instance()
MyClass = MyClass()
MyClass.class_method()