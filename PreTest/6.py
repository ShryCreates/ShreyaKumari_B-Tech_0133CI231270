f=open("report.txt","w")
f.write("Rahul-85\nPriya-90\nRohan-78\nSneha-92\nAmit-65")
f.close()
print("File created")

try:
    f=open("report.txt","r")
    lines=f.readlines()
    for line in lines:
       name,marks=line.strip().split("-")
       if int(marks)>80:
          print(f"{name}:{marks}")
except FileNotFoundError:
    print("File not found")          
finally:
    print("Completed")        