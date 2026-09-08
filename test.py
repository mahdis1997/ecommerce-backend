import requests

url = "https://dummyjson.com/products"

response = requests.get(url, params={"limit": 5})

print(response.status_code)

data = response.json()

for product in data["products"]:
    print(product["id"], product["title"], product["price"])