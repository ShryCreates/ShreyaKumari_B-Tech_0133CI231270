import json

students=[
    {"name":"Rahul",
     "age":20,
     "city":"Bhopal",
     "marks":80},
    
    {"name":"Raj",
     "age":22,
     "city":"Delhi",
     "marks":60},
    
    {"name":"Rohan",
     "age":25,
     "city":"Agra",
     "marks":95},
]

with open("student.json","w") as f:
    json.dump(students,f)
    
print("JSON file created")

f=open("student.json","r")
try:
    with open("student.json","r") as f:
        students_data=json.load(f)
        print("students with more than 75 marks")
        for student in students_data:
            if student["marks"]>75:
                print(f"{student['name']},{student['city']},{student['marks']}")
except FileNotFoundError:
    print("File not found")
