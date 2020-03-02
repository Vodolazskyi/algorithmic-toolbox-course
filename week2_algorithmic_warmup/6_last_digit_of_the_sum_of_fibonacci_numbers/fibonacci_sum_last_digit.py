# Uses python3
import sys


def fibonacci_sum_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum_ = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum_ += current

    return sum_ % 10


def pisano_period(m: int) -> int:
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_sum(n: int) -> int:
    n = n % pisano_period(10)
    return fibonacci_sum_naive(n)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
