from store import Store
from models.cart import Cart


class CLI:
    """Handle the command_line interface"""

    def __init__(self, store: Store):
        """Initialize the cli with a store."""

        self.store = store

        self.cart = Cart()

    def manager_menu(self)->str | None:
        """Handle the store manager mwnu."""

        username = input("username:")
        password = input("password:")

        if username != "admin" or password != "1234":

            print("login failed")

            return "main"

        while True:

            print("1.add product")
            print("2.list products")
            print("3.update products")
            print("4.Exit")

            choice = input("choice an option:")

            if choice == "1":

                name = input("product name:")

                try:

                    price = float(input("product price:"))

                    if price <= 0:
                        print("invalid price")
                        continue

                except ValueError:

                    print("invalid price")
                    continue

                try:

                    stock = int(input("product stock:"))

                    if stock < 0:
                        print("invalid stock")
                        continue

                except ValueError:

                    print("invalid stock")
                    continue

                self.store.add_product(name, price, stock)

            elif choice == "2":

                self.store.list_products()

            elif choice == "3":

                product_name = input("product name:")

                product = self.store.find_product(product_name)

                if product is None:

                    print("product not found")
                    continue

                try:

                    new_price = float(input("new price:"))

                    if new_price <= 0:
                        print("invalid price")
                        continue

                except ValueError:

                    print("invalid price")
                    continue

                try:

                    new_stock = int(input("new stock:"))

                    if new_stock < 0:
                        print("invalid stock")
                        continue

                except ValueError:

                    print("invalid stock")
                    continue

                product.price = new_price
                product.stock = new_stock

                print("product updated")

            elif choice == "4":

                return "exit"

            else:

                print("invalid choice")
 
    def customer_menu(self) -> str | None:
        """Handle the custemer menu."""

        while True:

            print("customer portal")

            print("avaiblable products")

            self.store.list_products()

            print("1.add item to cart")

            print("2.Remove item from cart")

            print("3.view cart")

            print("4.check out")

            print("5.return to main menu")

            choice = input("choice an option:")

            if choice == "1":

                product_name = input("product name:")

                try:

                    quantity = int(input("quantity:"))

                except ValueError:

                    print("invalid quantity")

                    continue

                product = self.store.find_product(product_name)

                if product is None:

                    print("product not found")

                else:

                    self.cart.add_to_cart(product, quantity)

            elif choice == "2":

                product_name = input("product name:")

                self.cart.remove_from_cart(product_name)

            elif choice == "3":

                self.cart.view_cart()

            elif choice == "4":

                if not self.cart.items:

                    print("cart is empty")

                    continue

                self.cart.view_cart()

                total = self.cart.total_price()

                print(f"total price: ${total:.2f}")

                print("thank you for your purchase!")

                self.cart.items.clear()

            elif choice == "5":

                return "main"

            else:

                print("invalid choice")