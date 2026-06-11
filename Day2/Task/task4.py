class BankAccount:
    __balance=5000
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited:{amount}.Balance:{self.__balance}")
        
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
            print(f"Withdrawn:{amount}.Balance:{self.__balance}")    
                
    def get_balance(self):
        print(f"Balance:{self.__balance}")
                