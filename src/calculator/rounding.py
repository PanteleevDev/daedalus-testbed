from decimal import ROUND_HALF_UP, Decimal


def round_to(x: float, n: int) -> float:
    """Round ``x`` to ``n`` digits using half-up (round-half-away-from-zero).

    ``n`` is the number of digits after the decimal point, mirroring the
    built-in ``round``. Positive ``n`` rounds to decimal places, ``n == 0``
    rounds to the nearest integer, and negative ``n`` rounds to tens,
    hundreds, etc.

    Unlike Python's built-in ``round`` (which uses banker's rounding),
    exact ``.5`` boundaries are always rounded away from zero, e.g.
    ``round_to(2.5, 0) == 3.0`` and ``round_to(-2.5, 0) == -3.0``.
    """
    quantum = Decimal(1).scaleb(-n)
    result = Decimal(str(x)).quantize(quantum, rounding=ROUND_HALF_UP)
    return float(result)
