from dataclasses import dataclass, field
from typing import List
from models.dimensions import Dimensions
from models.meta import Meta
from models.review import Review

@dataclass
class Product:
    id: int
    title: str
    description: str
    category: str
    price: float
    discount_percentage: float = field(metadata={'alias':'discountPercentage'})
    rating: float
    stock: int
    tags: List[str]
    sku: str
    weight: int
    dimensions: Dimensions
    warranty_information: str = field(metadata={'alias':'warrantyInformation'})
    shipping_information: str = field(metadata={'alias':'shippingInformation'})
    availability_status: str = field(metadata={'alias':'availabilityStatus'})
    reviews: List[Review]
    return_policy: str
    minimum_order_quantity: int
    meta: Meta
    images: List[str]
    thumbnail: str
    brand: str = None