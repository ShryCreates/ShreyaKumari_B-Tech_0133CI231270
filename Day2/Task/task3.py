from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Square(Shape):
    def area(self):
        print("Square area=side*side")
        
    def perimeter(self):
        print("Square perimeter=4*side")
        
class Circle(Shape):
    def area(self):
        print("Circle area=pi*r*r")   
        
    def perimeter(self):
        print("Circle perimeter=2*pi*r")  
        
s=Square()
s.area()
s.perimeter()
c=Circle()
c.area()
c.perimeter()                     