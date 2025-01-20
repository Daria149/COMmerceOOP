import pytest

from src.lawngrass import LawnGrass
from src.product_and_category import Category, Product
from src.smartphone import Smartphone


@pytest.fixture
def category_sm():
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    return category_smartphones


@pytest.fixture
def product_sm():
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return new_product


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def for_test_middle_price():
    return Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [
            (Smartphone("Samsung Galaxy S23 Ultra", "Серый цвет", 18000.0, 5, 95.5, "S23 Ultra", 256, "Серый")),
            (Smartphone("Samsung Galaxy S23 Ultra", "200MP камера", 15000.0, 2, 95.5, "S23 Ultra", 256, "Серый")),
        ],
    )


@pytest.fixture
def for_test_middle_price_without_product():
    return Category("cc", "hh", [])
