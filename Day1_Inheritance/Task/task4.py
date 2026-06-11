class Vehicle:
    def start(self):
        print("Vechicle starts")
    def stop(self):
        print("Vehicle stops")
        
class Bus(Vehicle):
    def route(self):
        print("Follows this route")
        
class Bike(Vehicle):
    def wheelie(self):
        print("Have two wheels") 
        
class Car(Vehicle):
    def music(self):
        print("Can play music")
        
b=Bus()
bi=Bike()
c=Car()
b.start()
b.stop()
b.route()
bi.start()
bi.stop()
bi.wheelie()
c.start()
c.stop()
c.music()                         