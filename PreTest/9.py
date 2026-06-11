import requests

url="https://jsonplaceholder.typicode.com/users"

response=requests.get(url)
if response.status_code==200:
        data=response.json()
        for data in data:
            print(f"Name:{data['name']}")
            print(f"Email:{data['email']}")
            print(f"Phone:{data['phone']}")
            print(f"Company Name:{data['companyname']}")