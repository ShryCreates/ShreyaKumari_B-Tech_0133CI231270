class Employee:
    __salary=50000
    
    def increment(self):
        self.__salary+=10000
        
    def deduct(self):
        self.__salary-=5000
        
    def get_salary(self):
        print(self.__salary)
        
e=Employee()
e.increment()
e.deduct()
e.get_salary()     

e2=Employee()
e2.increment()
e2.deduct()
e2.get_salary()           