from models.cartitem import Cartitem
from models.product import Product


class Cart:
    """Represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart """
        self.items: list[Cartitem] = []
        self.total = 0

    def add_to_cart(self, product: Product, quantity):
        """Add a product to the cart"""

        if quantity <= 0:
            print("quantity must be greater than 0")
            return

        if quantity <= product.stock:

            for item in self.items:
                if item.product.name == product.name:
                    item.quantity += quantity
                    product.stock -= quantity
                    return

            item = Cartitem(product, quantity)
            self.items.append(item)
            product.stock -= quantity
            return

        print("not enough stock")

    def remove_from_cart(self, product_name):
        """Remove a product from the cart"""

        for item in self.items:
            if item.product.name == product_name:
                item.product.stock += item.quantity
                self.items.remove(item)
                return

        print("product not found in cart.")

    def view_cart(self):
        """Display the contents of the cart"""

        if not self.items:
            print("cart is empty.")
            return

        for item in self.items:
            print(item.product, "x", item.quantity)

    def total_price(self):
        """Calculate the total price of the cart"""

        total = 0

        for item in self.items:
            total += item.product.price * item.quantity

        return total