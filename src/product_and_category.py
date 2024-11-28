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
        self.price = price
        self.quantity = quantity


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
        self.products = products if products else []
        self.category_count += 1
        self.product_count += len(products) if products else 0
