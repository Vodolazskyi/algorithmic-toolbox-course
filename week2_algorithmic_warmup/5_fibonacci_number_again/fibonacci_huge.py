# Uses python3
import sys


def get_fibonacci_huge_naive(n: int, m: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def pisano_period(m: int) -> int:
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge(n: int, m: int) -> int:
    n = n % pisano_period(m)
    return get_fibonacci_huge_naive(n, m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
