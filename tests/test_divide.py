import pytest


def divide(a, b):
    return a / b


def test_divide():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)
    assert divide(1, 2) == 0.5
