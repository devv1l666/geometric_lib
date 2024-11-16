import math


def area(r) -> int:
    if r < 0:
        raise ValueError("Radius can't be negative or zero")

    return math.pi * r * r


def perimeter(r) -> int:
    if r < 0:
        raise ValueError("Radius can't be negative or zero")

    return 2 * math.pi * r
