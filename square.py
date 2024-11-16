def area(a) -> int:
    if a <= 0:
        raise ValueError("Value can't be negative or zero")

    return a ** 2


def perimeter(a) -> int:
    if a <= 0:
        raise ValueError("Value can't be negative or zero")

    return 4 * a
