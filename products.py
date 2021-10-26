class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased=False):
        if is_increased:
            print("The price is increased.")
            self.price += self.price * percent_change 
        else:
            print("The price is decresed.")
            self.price -= self.price * percent_change
        return self
    
    def print_info(self):
        print(f"name: {self.name}, category: {self.category}, price: ${self.price}")
        return self