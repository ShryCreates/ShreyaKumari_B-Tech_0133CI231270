class Teacher:
    def teach(self):
        print("She is teaching")
        
class Principal:
    def manage_school(self):
        print("He manages the school")
        
class HeadTeacher(Teacher,Principal):
    def take_assembly(self):
        print("Takes assembly")   
        
h=HeadTeacher()
h.teach()
h.manage_school()
h.take_assembly()               