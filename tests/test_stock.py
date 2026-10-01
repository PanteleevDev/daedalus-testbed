import pytest

from inventory import Item, Stock

PEN = Item("pen", "Pen", 150)
BOOK = Item("book", "Book", 1200)


def test_add_and_quantity() -> None:
    stock = Stock()
    stock.add(PEN, 3)
    stock.add(PEN, 2)
    assert stock.quantity("pen") == 5


def test_remove_more_than_available_fails() -> None:
    stock = Stock()
    stock.add(PEN, 1)
    with pytest.raises(ValueError):
        stock.remove("pen", 2)


def test_total_value() -> None:
    stock = Stock()
    stock.add(PEN, 2)
    stock.add(BOOK, 1)
    assert stock.total_value_cents() == 1500


@pytest.mark.parametrize("quantity", [0, -1])
def test_non_positive_quantity_rejected(quantity: int) -> None:
    with pytest.raises(ValueError):
        Stock().add(PEN, quantity)


def test_remove_last_unit_forgets_sku() -> None:
    stock = Stock()
    stock.add(PEN, 2)
    stock.add(BOOK, 1)
    stock.remove("pen", 2)
    assert stock.quantity("pen") == 0
    assert "pen" not in stock._quantities
    assert "pen" not in stock._items
    assert stock.total_value_cents() == 1200


def test_remove_partial_keeps_sku() -> None:
    stock = Stock()
    stock.add(PEN, 3)
    stock.remove("pen", 1)
    assert stock.quantity("pen") == 2
    assert "pen" in stock._quantities
    assert "pen" in stock._items
