import requests

from controllers.main_app import MainApp
from models.api_response import APIResponse
from dataclass_wizard import fromdict

response = requests.get('https://dummyjson.com/products')
data = response.json()

data_obj = fromdict(APIResponse, data)

for product in data_obj.products:
    print("ID:", product.id, "Titulo:", product.title, "Descripción:", product.description)
    print("Reviews:")
    for review in product.reviews:
        print(review.reviewer_name + ": " + review.comment)
    print("==============================")

if __name__ == "__main__":
    main_app = MainApp("Primera API Tkinter", "1000x600")