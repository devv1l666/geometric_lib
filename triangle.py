def area(a, b, c) -> float:
    s = (a + b + c) / 2
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Radius can't be negative or zero")

    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Radius can't be negative")

    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Radius can't be negative or zero")

    return a + b + c
