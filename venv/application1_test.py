import requests

response = requests.get("http://127.0.0.1:3001/Users")
print(response.json())

response = requests.get("http://127.0.0.1:3001/Users/1")
print(response.json())

response = requests.post("http://127.0.0.1:3001/Users",
              json={'username': 'fasiljaleel@gmail.com', 'email': 'abc@hotmail.com'})
print(response.json())

response = requests.get("http://127.0.0.1:3001/Users")
print(response.json())

response = requests.delete("http://127.0.0.1:3001/Users/2")
print(response.json())

response = requests.get("http://127.0.0.1:3001/Users")
print(response.json())


