import requests

data = {"name": "Laptop", "price": 999.99, "tax": 1.25}
response = requests.post("http://127.0.0.1:8000/create", json=data)

print(response.json())