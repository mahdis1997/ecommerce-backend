import requests

url = "https://dummyjson.com/products"
params={
    "limit":5
}
response = requests.get(url,params=params)
if response.status_code==200:
    data=response.json()
    product=data["products"]

    for i in product:
        print(i["title"],
        i["price"])
    print(response.status_code)


