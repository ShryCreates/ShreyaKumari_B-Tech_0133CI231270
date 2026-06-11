class LoginSystem:
    __password='python@123'
    __attempts=3
    
    def login(self,password):
        try:
            if password !=self.__password:
                self.__attempts-=1
                print(f"Wrong password. Remaining:{self.__attempts}")
                if self.__attempts == 0:
                   raise AccountLockedError("Your account is locked")
            else:
                print("Login successful")
        except AccountLockedError as e:
            print(e)
        finally:
            print("Login completed")
            
class AccountLockedError(Exception):
    pass
        
l=LoginSystem()
l.login("hello@gmail.com")
l.login("hello@gmail.com")
l.login("hello@gmail.com")
l.login("python@123")                   