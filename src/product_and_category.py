
class Product:
    """Класс, определяющий характеристики продукта."""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, parameters: dict):
        return cls(**parameters)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if int(new_price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif self.__price > new_price:
            approval = input("Новая цена ниже текущей. Подтвердите: подтверждаете: 'y', не подтверждвете: 'n' ___")
            if approval == "y" and new_price >= 0:
                self.__price = new_price
            else:
                self.__price = self.__price
        else:
            self.__price = self.__price


class Category:
    """Класс, определяющий характеристики категорий, содержащей продукты."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации класса Category."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.category_count += 1
        self.product_count += len(products) if products else 0

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products(self):
        return self.__products
