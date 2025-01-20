from src.baseproduct import BaseProduct
from src.exceptions import ZeroQuantityProduct
from src.printmixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс, определяющий характеристики продукта."""

    name: str
    description: str
    price: float
    quantity: float
    all_products_price: float

    def __init__(self, name, description, price, quantity, all_products_price=0):
        """Метод для инициализации класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.all_products_price = all_products_price
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            all_products_price = self.__price * self.quantity + other.__price * other.quantity
            return all_products_price
        raise TypeError

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

    def __str__(self):
        total_products_quantity = 0
        for product in self.__products:
            total_products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_products_quantity} шт."

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавить товар с нулевым количеством.")
            except ZeroDivisionError as e:
                print(str(e))
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print("Товар добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def productss(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
