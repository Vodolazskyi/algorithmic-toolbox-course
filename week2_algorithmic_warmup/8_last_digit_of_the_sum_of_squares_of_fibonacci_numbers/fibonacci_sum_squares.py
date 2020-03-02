# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum_ = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum_ += current * current

    return sum_ % 10


def get_fibonacci_last_digit(n: int) -> int:
    if (n <= 1):
        return n

    prev2 = 0
    prev1 = 1
    for i in range(2, n+1):
        res = (prev1 + prev2) % 10
        prev2 = prev1
        prev1 = res
    return res


def fibonacci_sum_squares(n: int) -> int:
    x = get_fibonacci_last_digit(n % 60)
    y = get_fibonacci_last_digit((n + 1) % 60)
    return (x * y) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
