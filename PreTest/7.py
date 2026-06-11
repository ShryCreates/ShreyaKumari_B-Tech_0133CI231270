#create
f=open("employees.txt","w")
f.write("Rahul\nMeena\nShiv")
f.close()
print("File created")

#read
f=open("employees.txt","r")
constant=f.read()
print(constant)
f.close()

#append
f=open("employees.txt","a")
f.write("\nRohit\nReena")
f.close()

#updated
f=open("employees.txt","r")
constant=f.read()
print("Updated:")
print(constant)
f.close()

#delete
import os
os.remove("employees.txt")
print("File deleted", not os.path.exists("employees.txt"))