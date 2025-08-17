def calculate_distance(p1: list, p2: list) -> float:
    """Return the distance between points p1 and p2.

    p1 and p2 are lists of the form [x, y], where the x- and y-coordinates are floats.

    >>> calculate_distance([0, 0], [3.0, 4.0])
    5.0
    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5