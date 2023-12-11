import pytest

from mypackage.utils import calculate_area


def test_area():
    assert calculate_area(1) == 3.14
    with pytest.raises(ValueError, match="Radius<0"):
        calculate_area(-1)
