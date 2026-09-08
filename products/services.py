import requests
from .models import Product
def get_products_from_api():
    url="https://dummyjson.com/products"
    response=requests.get(url,params={'limit':5})
    data = response.json()
    products=[]
    for product in data["products"]:
        products.append({
            "name":product["title"],
            "price":product["price"],
            "stock":product["stock"]
        })
    return products

def import_products():
    products=get_products_from_api()

    for product in products:
        if not Product.objects.filter(
                name=product["name"]
        ).exists():
            Product.objects.create(
                name=product["name"],
                price=product["price"],
                stock=product["stock"]
            )