from calculator import round_to


def test_round_to_positive_digits() -> None:
    assert round_to(123.456, 2) == 123.46


def test_round_to_zero_digits() -> None:
    assert round_to(2.5, 0) == 3.0


def test_round_to_negative_digits_tens() -> None:
    assert round_to(1250, -2) == 1300.0


def test_round_to_negative_digits_hundreds() -> None:
    assert round_to(1549, -2) == 1500.0


def test_round_to_half_up_negative_number() -> None:
    assert round_to(-2.5, 0) == -3.0


def test_round_to_half_up_decimal_boundary() -> None:
    assert round_to(2.345, 2) == 2.35


def test_round_to_differs_from_builtin_round_banker_rounding() -> None:
    assert round_to(2.5, 0) == 3.0
    assert round(2.5) == 2


def test_round_to_returns_float() -> None:
    assert isinstance(round_to(1, 0), float)
