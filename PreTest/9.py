import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    if response.status_code == 200:
        users = response.json()
        print("Users from Gwenborough:\n")
        for user in users:
            if user["address"]["city"] == "Gwenborough":
                print("Name    :", user["name"])
                print("Email   :", user["email"])
                print("Phone   :", user["phone"])
                print("Company :", user["company"]["name"])
                print("-" * 30)
    else:
        print("Failed to fetch data.")
        print("Status Code:", response.status_code)

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API.")

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
