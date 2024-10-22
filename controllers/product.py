from controllers.api_controller import APIController
from views.product_card import ProductCard


class ProductController:

    @classmethod
    def show_products_cards(cls, products_frame):
        products = APIController.fetch_api_data().products
        for product in products:
            product_card = ProductCard(products_frame, product)
            product_card.pack(side="left", padx=(10, 10), pady=(10, 10))
