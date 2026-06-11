import json

#Python dictionary
student={
    "name":"Rahul",
    "age":20,
    "marks":85,
}

#convert dictionary to json string
# json_data=json.dump(student)
# print(json_data)
# print(type(json_data))

with open("student.json","w") as f:
    json.dump(student,f)
    
print("JSON file created")    