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
