class Father:
    def property(self):
        print("Owns house")
        
class Son:
    def bike(self):
        print("Owns bike")
        
class Daughter(Father,Son):
    def car(self):
        print("Owns car") 
        
d=Daughter()
d.property()
d.bike()
d.car()        