def square(x: float) -> float:
    """Return square of a number"""
    return x ** 2

def square_of_sum(numbers: list) -> float:
    """Return square of sum of numbers"""
    total = sum(numbers)
    return square(total)

print(square_of_sum([2, 3, 4]))