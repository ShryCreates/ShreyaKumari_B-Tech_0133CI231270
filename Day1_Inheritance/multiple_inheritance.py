class Father:
    def property(self):
        print("Father owns house")
        
class Mother:
    def cooking(self):
        print("Mother cooks")   
        
class Son(Father,Mother):
    def play(self):
        print("Child plays")
        
s=Son()
s.play()
s.property()
s.cooking()                     