class Father:
    def property(self):
        print("Owns property")
    
    def business(self):
        print("Does business")
        
class Son(Father):
    def study(self):
        print("He studies")
        
class Daughter(Father):
    def dance(self):
        print("She dances")
        
class GrandChild(Son,Daughter):
    def gaming(self):
        print("Play games")
        
g=GrandChild()
g.property()
g.business()
g.study()
g.dance()
g.gaming()                                    