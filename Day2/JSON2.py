import requests

#Free fake api
url="https://jsonplaceholder.typicode.com/users/1"

response=requests.get(url)
data=response.json()

print(f"Name:{data['name']}")
print(f"Email:{data['email']}")
print(f"City:{data['address']['city']}")