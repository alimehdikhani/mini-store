class Product:
    """Represents a product in the store."""
    def __init__(self,name:str,price:float,stock:int):
        """Initialize a Product"""
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self)-> str:
        """Return a readable product description"""
        return f"{self.name} - ${self.price:.2f} (stock:{self.stock})"