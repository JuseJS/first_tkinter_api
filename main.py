import requests

from models.api_response import APIResponse
from dataclass_wizard import fromdict

response = requests.get('https://dummyjson.com/products')
data = response.json()

api_response = fromdict(APIResponse, data)

for producto in api_response.products:
    print("ID:", producto.id, "Titulo:", producto.title, "Descripción:", producto.description)

