from src.product_and_category import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color, all_products_price=0):
        super().__init__(name, description, price, quantity, all_products_price)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            all_products_price = self.price * self.quantity + other.price * other.quantity
            return all_products_price
        raise TypeError
