from controllers.api_controller import APIController
from views.product_card import ProductCard


class ProductController:

    @classmethod
    def show_products_cards(cls, products_frame, main_controller):
        products = APIController.fetch_api_data().products
        for product in products:
            product_card = ProductCard(products_frame, product, main_controller)
            product_card.pack(side="left", padx=(10, 10), pady=(10, 10))
