from models.product import Product
class Cartitem:
    """Represents a product item in the cart"""
    def __init__(self,product:Product,quantity:int):

        self.product = product
        self.quantity = quantity
