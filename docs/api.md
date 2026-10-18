# Public API

`inventory` exports `Item` and `Stock`.

## Item

`Item(sku: str, name: str, unit_price_cents: int)` — an immutable product description.

## Stock

Quantities per SKU, kept in memory.

- `add(item: Item, quantity: int) -> None` — adds `quantity` units of `item`. A non-positive
  quantity raises `ValueError`.
- `remove(sku: str, quantity: int) -> None` — removes `quantity` units. A non-positive quantity or
  more than available raises `ValueError`.
- `quantity(sku: str) -> int` — units of `sku` in stock, `0` for an unknown SKU.
- `total_value_cents() -> int` — the sum of unit price times quantity over all SKUs.
