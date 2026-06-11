class Person:
    def walk(self):
        print("He is walking")
    def talk(self):
        print("He is talking")
        
class Student(Person):
    def study(self):
        print("He is studying")
    def attend_class(self):
        print("He is attending class")
        
s=Student()
s.walk()
s.talk()
s.study()
s.attend_class()                        