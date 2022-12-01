from ShoppingClass.cartaction import CartAction
from ShoppingClass.product import Product
from ShoppingClass.user import User
from collections import Counter
import json


class Shopping(CartAction, Product, User):
    # Set initial data
    def __init__(self):
        User.__init__(self)
        Product.__init__(self)

    def show_cart(self):
        products_in_cart = self.cart_detail()
        total = 0
        print("\n\n")
        print("Table: Cart")
        print(f"Name of user : {self._name}")
        print("--------------------------------------------------------------------------------------------------")
        print("ID                 NAME                       PRICE              AMOUNT                SUM")
        print("--------------------------------------------------------------------------------------------------")
        for product in products_in_cart:
            sum_price = float(product['price']) * float(product['amount'])
            print("{pid:2}{product_name:^40}{price:>10,.2f}{amount:^32}{sumprice:>10,.2f}".format(pid=product['id'],
                                                                                                  product_name=product[
                                                                                                      'name'],
                                                                                                  price=float(
                                                                                                      product['price']),
                                                                                                  amount=product[
                                                                                                      'amount'],
                                                                                                  sumprice=sum_price))
            total += sum_price
        print("--------------------------------------------------------------------------------------------------")
        print(f"                                                                 Total              {total:>10,.2f}")
        print(
            "--------------------------------------------------------------------------------------------------\n\n")

    # Get detail of products ( id is the same as the cart ).
    def cart_detail(self):
        cart_products_count = Counter(self._cart)  # Counting number of each the products in the cart.
        cart = self.products(self._cart)
        for i, c in enumerate(cart):
             cart[i]["amount"] = cart_products_count[cart[i]["id"]]  # Merge into data products
        return cart  # Return data products


