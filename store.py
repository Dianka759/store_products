class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = []
        # self.product = Product()

    def add_product(self, new_product):
        self.products.append(new_product.name)
        print(f"Products list: {self.products}")
        return self

    def sell_product(self, id):
        print(self.products.pop(id), "was sold.")
        print(f"Products list: {self.products}")
        return self

    # def inflation(self, percent_increase):
    #     for i in range(len(self.products)):
    #         self.products[i].update_price(percent_increase)

# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)

    # def set_clearance(self, category, percent_discount):
    #     return self

    def list_products(self):
        print(f"Products list: {self.products}")