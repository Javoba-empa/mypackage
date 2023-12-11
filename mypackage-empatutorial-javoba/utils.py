from .geometry.geometry import Point


def distance(p1: "Point", p2: "Point") -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def calculate_area(radius: float) -> float:
    """Calculates the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius<0")

    area = 3.14 * radius**2
    return area
