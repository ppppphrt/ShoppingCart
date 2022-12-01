class CartAction:

    def __init__(self):

        self._cart = []
        self._products = None

    def product_to_cart(self, pid):
        print(f'Add a product success !')
        # if [pid == product['id'] for product in self._products]:
        #     print("No the product in database")


    def product_out_cart(self, pid):

        self._cart.remove(pid)  # Remove it
        print('Remove a product success !')





