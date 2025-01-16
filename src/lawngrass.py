from src.product_and_category import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color, all_products_price=0):
        super().__init__(name, description, price, quantity, all_products_price)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            all_products_price = self.price * self.quantity + other.price * other.quantity
            return all_products_price
        raise TypeError
