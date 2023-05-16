"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    """Создает объект Item."""
    return Item(name="Phone", price=19999.9, quantity=5)


@pytest.fixture
def item2():
    """Создает объект Item."""
    return Item(name="TV", price=30000, quantity=2.0)


def test_class_attributes():
    assert isinstance(Item.pay_rate, float)
    assert Item.pay_rate < 1
    assert isinstance(Item.all, list)


def test_init(item1, item2):
    """Тестирует конструктор Item."""

    assert isinstance(item1.name, str)
    assert isinstance(item1.price, float)
    assert isinstance(item1.quantity, int)

    assert isinstance(item2.name, str)
    assert isinstance(item2.price, float)
    assert isinstance(item2.quantity, int)


def test_calculate_total_price(item1, item2):
    """Тестирует метод calculate_total_price."""
    assert item1.calculate_total_price() == 19999.9 * 5
    assert item2.calculate_total_price() == 30000 * 2.0


def test_apply_discount(item1, item2):
    """Тестирует метод apply_discount."""
    item1.apply_discount()
    assert item1.price == round(19999.9 * 0.85, 2)

    item2.apply_discount()
    assert item2.price == round(30000 * 0.85, 2)
