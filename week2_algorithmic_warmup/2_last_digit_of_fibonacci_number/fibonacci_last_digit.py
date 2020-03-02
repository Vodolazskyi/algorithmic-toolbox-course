# Uses python3
import sys


def get_fibonacci_last_digit_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


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


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
