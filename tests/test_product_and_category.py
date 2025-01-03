from itertools import product
from unittest.mock import patch

import pytest

from src.product_and_category import Category, Product


@pytest.fixture
def test_product_fruit():
    return Product(name="apple", description="gold", price=100.20, quantity="10")


@pytest.fixture
def test_2_product_fruit():
    return Product(name="orange", description="sweet", price=100.00, quantity="20")


@pytest.fixture
def test_category_fruit():
    return Category(name="fruit", description="gold", products=["apple", "pear", "orange"])


@pytest.fixture
def test_2_category_fruit():
    return Category(name="Смартфоны", description="новые", products=["apple", "samsung", "nokia"])


def test_3_category_fruit():
    category1 = Category(name="healthy fruit", description="good and fresh", products=["apple", "pear", "orange"])
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_new_product():
    p = Product.new_product({"name": "Samsung", "description": "256GB, Серый цвет", "price": 50000.0, "quantity": 5})
    assert (f"{p.name}, {p.description}, {p.price}, {p.quantity}") == "Samsung, 256GB, Серый цвет, 50000.0, 5"


@patch("builtins.input")
def test_price_setter(mock_input, capsys):
    new_product = Product.new_product(
        {"name": "Samsung", "description": "256GB, Серый цвет", "price": 100.0, "quantity": 5}
    )
    new_product.price = 50
    message = capsys.readouterr()
    mock_input.return_value = "n"
    assert message.out.strip() == ""
    assert new_product.price == 100

    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_add_product_in_products():
    product1 = Product("QLED 4K", "Фоновая подсветка", 123000.0, 7)
    assert (
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
        == "QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )


@pytest.fixture
def test_all_products_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product1.__price * product1.quantity + product2.__price * product2.quantity


def test_product_str():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_str():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_price_add_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    all_products_price = product1.price * product1.quantity + product2.price * product2.quantity
    assert all_products_price == 2580000.0


def test_add_product(category_sm, product_sm):
    category_sm.add_product(product_sm)
    assert category_sm.description == "Высокотехнологичные смартфоны"
    assert Category.product_count == 1
    category_sm.add_product(product_sm)
    assert Category.product_count == 2


def test_add_product_error(category_sm, product_sm):
    with pytest.raises(TypeError):
        category_sm.add_product(1)
