class Father:
    def property(self):
        print("Father owns flat")
        
class Son(Father):
    def bike(self):
        print("Son owns bike")    
        
s=Son()
s.bike()
s.property()            