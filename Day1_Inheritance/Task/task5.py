class Animal:
    def breathe(self):
        print("Animal breathes")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
class Cat(Animal):
    def meow(self):
        print("Cat meows")
        
class Pet(Dog,Cat):
    def play(self):
        print("Both plays together")
       
p=Pet()
p.breathe()
p.bark()
p.meow()        
p.play()                            