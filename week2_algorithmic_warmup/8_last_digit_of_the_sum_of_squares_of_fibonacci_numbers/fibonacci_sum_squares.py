# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum_     = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum_ += current * current

    return sum_ % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
