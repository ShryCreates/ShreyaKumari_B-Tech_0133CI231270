#create and write file
f= open("test.txt","w")
f.write("Hello World")
f.close()
print("File created")

#read file
f=open("test.txt","r")
constant=f.read()
print(constant)
f.close()

#append file
f=open("test.txt","a")
f.write("\nNew Line added")
f.close()