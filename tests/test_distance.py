from mypackage_empatutorial_javoba.geometry.geometry import Point
from mypackage_empatutorial_javoba.utils import distance


def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(0, 2)

    assert distance(p1, p2) == 5
    assert distance(p1, p3) == 2
