a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by 0") 
 
try:
    num=int("abc")
except ValueError:
    print("This is not a no.")        
    
# handling multiple exceptions   
try:
    num=int(input("Enter no."))
    print(10/num)
except ValueError:
    print("Enter no. Don't enter text")          
except ZeroDivisionError:
    print("Cannot divide by 0")    
finally:
    print("It will execute anyhow")     