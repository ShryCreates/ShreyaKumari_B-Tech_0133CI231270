class Person:
    __name="Rahul"  #private
    
    def get_name(self):
        print(self.__name)
        
p=Person()
p.get_name()        