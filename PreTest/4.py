class AgeVerification:
    def set_age(self,age):
            try:
                if age<0:
                    raise ValueError("Age can never be negative")
                elif age<18:
                    raise UnderAgeError("Underaged") 
                elif age>100:
                    raise InvalidAgeError("Invalid age")
                else:
                    print("Valid age!")
            except ValueError as a:
                print(a)
            except UnderAgeError as b:
                print(b)
            except InvalidAgeError as c:
                print(c)
            finally:
                print("Age verified")
                
class UnderAgeError(Exception):
    pass                       

class InvalidAgeError(Exception):
    pass

a=AgeVerification()
a.set_age(-8)           
a.set_age(4)    
a.set_age(300)    
a.set_age(40)                    