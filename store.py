from models.product import Product
class Store:
    """Manage the store inventory"""
    def __init__(self):
        """Initualize an empty product list """
        self.products:list[Product] = []


    def add_product(self,name:str,price:float,stock:int) -> None:
        """Add a new product to the store"""

        product = Product(name,price,stock)
        self.products.append(product)


    def list_products(self) -> None:
        """Display all products in the store"""

        if not self.products:
            print("no product avalibale.")

        for product in self.products:

            print(product)


    def find_product(self,name:str) -> Product | None:
        """Find a product by name"""

        for product in self.products:
            if product.name == name:
                return product

        return None



