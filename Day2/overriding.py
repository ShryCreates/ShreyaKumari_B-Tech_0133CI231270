# Overriding uses inheritance with same function name with different functionality

class Women:
    def women(self):
        print("Someone's mom")
        
class Employee(Women):
    def women(self):
        print("She is an employee")
        
e=Employee()
e.women()        