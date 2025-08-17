lyrics = [
    "It's pourin' in, you're laid on the floor again",
    "One knock at the door and then",
    "We both know how the story ends",
    "You can't win if your white flag's out when the war begins",
    "Aimin' so high, but swingin' so low",
    "Tryna catch fire, but feelin' so cold",
    "Hold it inside, and hope it won't show",
    "I'm sayin' it's not, but inside I know"
]

print(*lyrics, sep="\n")

print(abs(-10))
print(round(5.4))
print(round(2.335, 2))

def square(x: float) -> float:
    """Return x squared.

    >>> square(3.0)
    8.0
    >>> square(2.5)
    6.25
    """
    return x ** 2

print(square(4))

print(square.__doc__)
help(square)