from models.product import Product
from models.client import Client
class Sale:
    def __init__(self, product:Product, client:Client, qty:int):
        self.product_name  = product.name
        self.product_price = product.price
        self.client_dni    = client.dni
        self.qty           = qty
