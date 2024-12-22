import pytest

from src.iter_products import ProductsIterator
from src.product_and_category import Category, Product


@pytest.fixture
def test_iter_products(second_product):
    return ProductsIterator(second_product)


def test_2_iter_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )
    iterator = ProductsIterator(category1)

    for i in iterator:
        assert str(i) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_3_iter_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    iterator = ProductsIterator(category1)

    for i in iterator:
        assert i == StopIteration
