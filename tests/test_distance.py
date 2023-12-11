from mypackage.geometry.geometry import Point
from mypackage.utils import distance


def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert distance(p1, p2) == 5
    p3 = Point(0, 2)
    assert distance(p1, p3) == 2
