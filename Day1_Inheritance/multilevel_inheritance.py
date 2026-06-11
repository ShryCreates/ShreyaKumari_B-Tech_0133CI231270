class Grandfather:
    def money(self):
        print("Owns 10000 money")
        
class Father(Grandfather):
    def car(self):
        print("Owns BMW car")
        
class Son(Father):
    def bike(self):
        print("Owns bike")
        
s=Son()
s.bike()
s.car()
s.money()                        