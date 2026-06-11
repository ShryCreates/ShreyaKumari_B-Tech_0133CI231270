class Father:
    def property(self):
        print("Owns house")
        
class Son(Father):
    def bike(self):
        print("Owns bike")
        
class Daughter(Father):
    def car(self):
        print("Owns car")   
        
s=Son()
d=Daughter()
s.property()
s.bike()
d.property()
d.car()                    