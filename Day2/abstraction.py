from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class Gpay(Payment):
    def pay(self):
        print("Paid via Gpay")
    
class Cash(Payment):
    def pay(self):
        print("Paid via cash")      
        
g=Gpay()
g.pay()
c=Cash()
c.pay()        