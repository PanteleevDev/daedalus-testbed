from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    unit_price_cents: int


class Stock:
    """Quantities per SKU."""

    def __init__(self) -> None:
        self._items: dict[str, Item] = {}
        self._quantities: dict[str, int] = {}

    def add(self, item: Item, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._items[item.sku] = item
        self._quantities[item.sku] = self._quantities.get(item.sku, 0) + quantity

    def remove(self, sku: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        available = self._quantities.get(sku, 0)
        if quantity > available:
            raise ValueError(f"not enough {sku}: {available} available")
        remaining = available - quantity
        if remaining == 0:
            self._quantities.pop(sku, None)
            self._items.pop(sku, None)
        else:
            self._quantities[sku] = remaining

    def quantity(self, sku: str) -> int:
        return self._quantities.get(sku, 0)

    def total_value_cents(self) -> int:
        return sum(self._items[sku].unit_price_cents * q for sku, q in self._quantities.items())
