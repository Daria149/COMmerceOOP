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
def test_price_setter(capsys, mock_input):
    new_product = Product.new_product(
        {"name": "Samsung", "description": "256GB, Серый цвет", "price": 100.0, "quantity": 5}
    )
    new_product.price = 50
    message = capsys.readouterr()
    assert message.out.strip() == "Новая цена ниже текущей. Подтвердите: подтверждаете: 'y', не подтверждвете: 'n' ___"
    mock_input.return_value = "y"
    assert new_product.price == 50

    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    new_product.price = 5000.0
    assert new_product.price == 5000.0


def test_products_list():
    product1 = Product("QLED 4K", "Фоновая подсветка", 123000.0, 7)
    assert (
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
        == "QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )
